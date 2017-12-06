# coding=utf-8

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

import data_mgr


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

    all_md_df = data_mgr.get_hs300_md_features()
    all_md_df['target'] = 4 - all_md_df['target']
    names = ["ma5_10", "ma10_20", "ma5_20", "ma_desc", "ma_score"]
    # names = ["mrate5", "mrate10", "mrate_avg", "mrate_diff"]

    all_md_df = all_md_df.sort_values(by=["rate_sum_5_10"], ascending=[0]).head(2000)


    # print(all_md_df)
    x1 = all_md_df["target"] != 2
    df = all_md_df.ix[x1, names + ["target"]]

    sb.pairplot(df.dropna(), hue='target')
    plt.show()



def main2():

    all_md_df = data_mgr.get_hs300_md_features()
    all_md_df['target'] = 4 - all_md_df['target']
    names = ["ma5_10", "ma10_20", "ma5_20", "ma_desc", "ma_score"]
    #names = ["mrate5", "mrate10", "mrate_avg", "mrate_diff"]

    #x1 = (all_md_df["ma5_20"] <= -28) | (all_md_df["ma_desc"] <= -13)
    df = all_md_df.ix[:, names + ["target"]]
    df["fii1"] = 0

    for idd, row in df.iterrows():
        p1 = (-10, -20)
        p2 = (-23, -9)
        tp = (row['ma10_20'], row['ma5_10'])
        flg = xyz(p1, p2, tp)

        if flg:
            df.loc[idd, "fii1"] = 1

    df["fii2"] = 0
    for idd, row in df.iterrows():
        p1 = (-16, 0)
        p2 = (16, 130)
        tp = (row['ma_desc'], row['ma5_10'])
        flg = xyz(p1, p2, tp)

        if flg:
            df.loc[idd, "fii2"] = 1


    df = all_md_df.ix[(df['fii1'] >=1) | (df['fii2'] >=1) , names + ["target"]]
    print(df.describe())
    sb.pairplot(df.dropna(), hue='target')
    plt.show()






if __name__ == '__main__':
    main1()