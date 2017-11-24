# coding=utf-8
import pandas as pd
import tushare as ts
import matplotlib.pyplot as pt
from zibiao.zb import ZB


def main1():

    stock_data = ts.get_hist_data("600238", start="2017-07-01")
    stock_data.sort_index(ascending=True, inplace=True)
    #print(stock_data)
    kdj = ZB.kdj(stock_data)

    kdj.plot()
    pt.show()


def main2():
    stock_data = ts.get_hist_data("600238", start="2017-07-01")
    stock_data.sort_index(ascending=True, inplace=True)

    mdi = ZB.mdi(stock_data)

    mdi.plot()
    pt.show()
    print(mdi)




if __name__ =="__main__":

    main2()