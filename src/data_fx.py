# coding=utf-8

import pickle

import os
import re

import pandas as pd
import tushare as ts
import seaborn as sb
import matplotlib.pyplot as plt

from data_mgr import get_hs300_md_features



if __name__ == '__main__':
    all_df = get_hs300_md_features()

    """
    all_df = all_df.sort_values(["rate_sum_5_10"]).tail(20000)
    all_df = all_df.sort_values(["rate_sum_3_10"]).tail(10000)
    all_df = all_df.sort_values(["ma_desc"]).head(5000)
    """

    #"""
    all_df = all_df.sort_values(["ma_desc"]).head(15000)
    #all_df = all_df.sort_values(["ma5_20"]).head(10000)
    all_df = all_df.sort_values(["ma5_10"]).head(6000)
    #"""

    print(all_df.describe())
    # x1 = all_df['ma_desc'] <= -18
    # x2 = (all_df['target'] >= 2) & (all_df['target'] < 2.1)
    names = ["ma5_10", "ma10_20", "ma5_20", "ma_desc", "ma_score"]
    all_df = all_df.ix[all_df['target'].isin([1,3]), names + ['target']]
    all_df.ix[:, "target"] = 4 - all_df['target']

    #print(all_df.describe())

    sb.pairplot(all_df, hue="target")
    plt.show()



