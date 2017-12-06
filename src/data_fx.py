# coding=utf-8

import pickle

import os
import re

import pandas as pd
import tushare as ts
import seaborn as sb
import matplotlib.pyplot as plt

from data_mgr import get_hs300_md_features



def xyz(p1, p2, tp):
    """
    (p1.x - p2.x) / (p1.y - p2.y) * (p.y - p2.y) + p2.x
    点在线的左边还是右边
    左=true, 右=false

    """

    x1, y1 = p1
    x2, y2 = p2

    x, y = tp

    #tmp = (y1 – y2) *x + (x2 – x1) *y + x1 * y2 – x2 * y1
    tmpx = (x1-x2) / (y1-y2) * (y-y2) + x2
    if tmpx > x: return True
    return False


def main1():
    all_df = get_hs300_md_features()

    """
    all_df = all_df.sort_values(["rate_sum_5_10"]).tail(20000)
    all_df = all_df.sort_values(["rate_sum_3_10"]).tail(10000)
    all_df = all_df.sort_values(["ma_desc"]).head(5000)
    """

    #"""
    #all_df = all_df.sort_values(["ma_desc"]).head(15000)
    all_df = all_df.sort_values(["ma5_10"]).head(15000)
    all_df = all_df.sort_values(["ma5_20"]).head(6000)
    #"""

    print(all_df.describe())
    # x1 = all_df['ma_desc'] <= -18
    # x2 = (all_df['target'] >= 2) & (all_df['target'] < 2.1)
    names = ["ma5_10", "ma10_20", "ma5_20", "ma_desc"]
    all_df = all_df.ix[all_df['target'].isin([1, 3]), names + ['target']]
    all_df.ix[:, "target"] = 4 - all_df['target']

    print(all_df.describe())

    sb.pairplot(all_df, hue="target")
    plt.show()



def main2():
    names = ["ma5_10", "ma10_20", "ma5_20", "ma_desc"] + ['target']
    all_df = get_hs300_md_features()
    all_df = all_df.loc[:, names]

    #all_df = all_df.ix[(all_df['ma5_20'] <= -25) | (all_df['ma_desc'] <= -13)]

    all_df['fii1'] = 0
    p1 = (-25, -3.5)
    p2 = (-5.5, -19)

    for idd, row in all_df.iterrows():
        tp = (row['ma10_20'], row['ma5_10'])
        flg = xyz(p1, p2, tp)
        if flg:
            all_df.loc[idd, "fii1"] = 1

    all_df = all_df.ix[(all_df['fii1'] == 1) | (all_df['ma5_20'] <= -25) | (all_df['ma_desc'] <= -13)]
    print(all_df)
    #print(all_df.describe())

    sb.pairplot(all_df, hue="target")
    plt.show()



def ma_md2(df):

    names = ["ma5_10", "ma10_20", "ma5_20", "ma_desc"]
    df = df.ix[:, names]
    df['fii1'] = 0
    df['md2_sign']


if __name__ == '__main__':

    main2()