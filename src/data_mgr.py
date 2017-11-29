# coding=utf-8

import pickle

import os
import re

import pandas as pd
import tushare as ts
import matplotlib.pyplot as pt
from zibiao.zb import ZB

ctx = {"sum": 0}


def download_k_data(code):

    stock_data = ts.get_k_data(code, start="2010-01-01")

    stock_data.set_index("date", inplace=True)
    stock_data.sort_index(ascending=True, inplace=True)
    stock_data['p_change'] = 0

    stock_data['p_change'] = ((stock_data['close'] - stock_data['close'].shift(1)) / stock_data['close'].shift(1) * 100).round(2)

    stock_data = stock_data.ix[1:]
    with open("h_datas\\%s.model" % code, "wb+") as mfile:
        pickle.dump(stock_data, mfile)


def get_k_data(code):
    with open("h_datas\\%s.model" % code, "rb") as mfile:
        stock_data = pickle.load(mfile)
        return stock_data


def target_rate(code):
    #stock_data = ts.get_hist_data("000001", start="2010-01-01")
    stock_data = get_k_data(code)
    stock_data.sort_index(ascending=True, inplace=True)

    signal_df = ZB.buy_signal(stock_data)
    target_df = ZB.zf_target(stock_data)

    df = pd.concat([signal_df, target_df], axis=1)

    # df.drop(['2017-11-28'], axis=0, inplace=True)
    # for index, row in df.iterrows():

    x = df.ix[df['signal'] > 0]
    y = x.ix[x['target'] >= 3]

    ctx["sum"] += len(x)
    rat = len(y) / len(x) * 100
    return rat


def iter_hs300_target_rate():
    rat_list = []
    for filename in os.listdir("h_datas"):
        find = re.findall("(\d+)\.model",  filename)
        code = find[0] if find else ""
        if not code: continue
        rat = target_rate(code)
        rat_list.append(rat)

    avg = sum(rat_list) / len(rat_list)

    print(avg)


def iter_hs300s(func):
    for filename in os.listdir("h_datas"):
        find = re.findall("(\d+)\.model",  filename)
        code = find[0] if find else ""
        if not code: continue
        ret = func(code)
        yield ret


def download_hs300s():

    retrys = ["601163", "601881", "600583", "600369",
              "600827", "600485", "600415", "600074", "601198", "601800", "601169", "600804", "601607", "600023"]

    for code, row in ts.get_hs300s().set_index("code").iterrows():
        if code not in retrys: continue
        print(row['name'], "  ", code)
        download_k_data(code)


def extract_md_features(code):
    """

    :param code:
    :return:
    """
    stock_data = get_k_data(code)
    stock_data.sort_index(ascending=True, inplace=True)

    ma_df = ZB.ma(stock_data, m4=0)

    stock_data = pd.concat([stock_data, ma_df], axis=1)

    signal_df = ZB.buy_signal(stock_data).ix[20:-6]
    target_df = ZB.zf_target(stock_data)

    ma_diff_desc_df = ZB.ma_diff_desc(stock_data)
    simple_duokong_df = ZB.simple_duokong(stock_data)
    vol_duokong_df = ZB.vol_duokong(stock_data)

    concat_list = [signal_df, target_df, simple_duokong_df, vol_duokong_df, ma_diff_desc_df]
    md_df = pd.concat(concat_list, axis=1)

    md_df = md_df.ix[md_df['signal'] > 0]
    # print(md_df)
    # print(x.describe())

    return code, md_df


def extract_hs300_md_features():
    hs300_md_features_dfs = []
    for code, md_df in iter_hs300s(extract_md_features):
        print(code)
        hs300_md_features_dfs.append(md_df)

    # 纵向合并
    all_df = pd.concat(hs300_md_features_dfs, axis=0, ignore_index=True)
    """
    all_df.to_csv("csv_files\\all_df.csv", index=False)

    with open("csv_files\\all_md_df.model", "wb+") as mfile:
        pickle.dump(all_df, mfile)
    """
    return all_df


def get_hs300_md_features():

    with open("csv_files\\all_md_df.model", "rb") as mfile:
        all_df = pickle.load(mfile)

    return all_df



if __name__ == '__main2__':
    code, df = extract_md_features("600369")

    print(df[["target", "signal"]].values)


if __name__ == '__main__':
    print(get_hs300_md_features().tail(10))