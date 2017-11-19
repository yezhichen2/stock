# coding=utf-8
import pandas as pd


class ZB(object):

    @classmethod
    def kdj(cls, stock_data):
        df = stock_data.loc[:, ["close", "low", "high"]]
        min_low = df['low'].rolling(window=9, min_periods=1).min()
        max_high = df['high'].rolling(window=9, min_periods=1).max()

        rsv = (df["close"] - min_low) / (max_high - min_low) * 100

        df["kdj_k"] = rsv.ewm(com=2).mean()
        df["kdj_d"] = df["kdj_k"].ewm(com=2).mean()
        df["kdj_j"] = 3 * df["kdj_k"] - 2 * df["kdj_d"]

        return df.loc[:, ["kdj_k", "kdj_d", "kdj_j"]]

    @classmethod
    def mdi(cls, stock_data):
        pass


