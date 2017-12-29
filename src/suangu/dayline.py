# coding=utf-8
import pandas as pd
from data_mgr import get_k_data
from zibiao.zb import ZB


def select_on_ma(st_df):
    """
    确保20或60均线有支撑
    :param st_df:
    :return:
    """
    name = "JX2060JC"
    ma_df = ZB.ma(st_df)

    ma_df["close"] = st_df["close"]
    ma_df[name] = (st_df["close"] >= ma_df["ma20"]) | (st_df["close"] >= ma_df["ma60"])

    return ma_df.ix[:, [name]]


def select_on_kdj(st_df):
    """
    J，K 同时向上， J 在中低位
    :param st_df:
    :return:
    """
    name = "KDJSELECT"
    kdj_df = ZB.kdj(st_df)

    x1 = kdj_df["kdj_j"] <= 70
    x2 = (kdj_df["kdj_j"] >= kdj_df["kdj_j"].shift(1)) & (kdj_df["kdj_k"] >= kdj_df["kdj_k"].shift(1))

    kdj_df[name] = x1 & x2

    return kdj_df.ix[:, [name]]


def select(st_df):
    name = "selected"
    x1_df = select_on_ma(st_df)
    x2_df = select_on_kdj(st_df)

    xx_df = pd.concat([x1_df, x2_df], axis=1)

    xx_df[name] = False
    xx_df.ix[xx_df['JX2060JC'] & xx_df['KDJSELECT'], name] = True
    return xx_df.ix[:, [name]]


if __name__ == '__main__':
    st_df = get_k_data("600115")
    df = select(st_df)
    print(df.ix[df["selected"]])

