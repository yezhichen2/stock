# coding=utf-8

import pandas as pd
import tushare as ts
import matplotlib.pyplot as pt
from zibiao.zb import ZB


def main2():
    stock_data = ts.get_hist_data("000001", start="2010-01-01")
    stock_data.sort_index(ascending=True, inplace=True)

    signal_df = ZB.buy_signal(stock_data)
    target_df = ZB.zf_target(stock_data)

    df = pd.concat([signal_df, target_df], axis=1)

    #df.drop(['2017-11-28'], axis=0, inplace=True)
    #print(df)

    #for index, row in df.iterrows():

    print("----------------------")
    x = df.ix[df['signal'] > 0]
    print(x)





if __name__ == '__main__':
    main2()


