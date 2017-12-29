# coding=utf-8
import pickle

import datetime

import os

import sys
import tushare as ts

import st_conf
from suangu import dayline, ma30line

start_date = "2017-01-01"


def _fix_p_change(st_df):
    st_df['p_change'] = 0
    st_df['p_change'] = ((st_df['close'] - st_df['close'].shift(1)) / st_df['close'].shift(1) * 100).round(2)


def get_day_st(code):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    fname = r"st_datas/day/{0}__{1}.model".format(code, today)
    if os.path.isfile(fname):

        with open(fname, "rb") as mfile2:
            stock_data = pickle.load(mfile2)
            return stock_data

    print("download %s ..." % code)
    stock_data = ts.get_k_data(code, start=start_date)

    stock_data.set_index("date", inplace=True)
    stock_data.sort_index(ascending=True, inplace=True)
    _fix_p_change(stock_data)

    stock_data = stock_data.ix[1:]

    with open(fname, "wb") as mfile:
        pickle.dump(stock_data, mfile)

    return stock_data


def select_day_line(code):
    st_df = get_day_st(code)

    slt_df = dayline.select(st_df)

    row = slt_df.tail(1).iloc[0]
    return row["selected"]


def get_30m_st(code):

    # start 在这个方法中不起作用
    stock_data = ts.get_k_data(code, start="", ktype="30")
    stock_data.set_index("date", inplace=True)
    stock_data.sort_index(ascending=True, inplace=True)

    _fix_p_change(stock_data)

    stock_data = stock_data.ix[1:]

    return stock_data


def iter_all_sts(st_codes, func):

    for code in st_codes:
        try:
            res = func(code)
            if res is not None: yield res

        except Exception as e:
            print(e)


def suan_gu():

    def xxx(code):
        selected = select_day_line(code)

        if selected:
            return code

    def yyy(code):
        st_df = get_30m_st(code)
        slt_df = ma30line.select(st_df)

        row = slt_df.tail(1).iloc[0]
        if row["selected"]: return code

    st_codes = [code for code, name in st_conf.zz500]
    selected_codes = [code for code in iter_all_sts(st_codes, xxx)]

    selected_codes = [code for code in iter_all_sts(selected_codes, yyy)]

    return selected_codes


if __name__ == '__main__':
    codes = suan_gu()

    print("\n\n")

    

    print(codes)





