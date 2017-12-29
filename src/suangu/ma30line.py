# coding=utf-8
import pandas as pd
from data_mgr import get_k_data
from zibiao.zb import ZB



def _cross(s1, s2):
    df_temp = pd.DataFrame({"a": s1, "b": s2})

    df_temp["cross"] = False
    df_temp.ix[(df_temp['a'].shift(1) <= df_temp['b'].shift(1)) & (df_temp['a'] > df_temp['b']), "cross"] = True
    return df_temp["cross"]


def select_on_ma(st_df):
    """

    :param st_df:
    :return:
    """
    name = "x1"
    ma_df = ZB.ma(st_df)

    ma_df["count"] = 0
    ma_df["close"] = st_df["close"]

    ma_df.ix[st_df["close"] >= ma_df["ma10"], "count"] += 1
    ma_df.ix[st_df["close"] >= ma_df["ma20"], "count"] += 1
    ma_df.ix[st_df["close"] >= ma_df["ma60"], "count"] += 1

    ma_df.ix[ma_df["ma10"] >= ma_df["ma10"].shift(1), "count"] += 1

    ma_df[name] = False
    ma_df.ix[ma_df["count"] >= 4, name] = True

    return ma_df.ix[:, [name]]


def select_on_dmi(st_df):
    """
    :param st_df:
    :return:
    """
    name = "x2"
    mdi_df = ZB.mdi(st_df)

    mdi_df["ca"] = _cross(mdi_df["ADX"], mdi_df["ADXR"])

    x1 = mdi_df["PDI"] > mdi_df["MDI"]

    mdi_df[name] = False

    mdi_df.ix[x1 & mdi_df["ca"], name] = True

    return mdi_df.ix[:, [name]]


def select(st_df):
    name = "selected"
    x1_df = select_on_ma(st_df)
    x2_df = select_on_dmi(st_df)

    xx_df = pd.concat([x1_df, x2_df], axis=1)

    xx_df[name] = False
    xx_df.ix[xx_df['x1'] & xx_df['x2'], name] = True
    return xx_df.ix[:, [name]]


if __name__ == '__main__':
    st_df = get_k_data("600115")
    # df = select_on_dmi(st_df)
    df = select(st_df)

    print(df.ix[df["selected"]])


