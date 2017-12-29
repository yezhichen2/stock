# coding=utf-8
import json

import pickle
import tushare as ts

import st_conf
from suangu2.pbb_estimation import PBB


def download_k_data(code):

    stock_data = ts.get_k_data(code, start="2010-01-01")

    stock_data.set_index("date", inplace=True)
    stock_data.sort_index(ascending=True, inplace=True)
    stock_data['p_change'] = 0

    stock_data['p_change'] = ((stock_data['close'] - stock_data['close'].shift(1)) / stock_data['close'].shift(1) * 100).round(2)

    stock_data = stock_data.ix[1:]

    return stock_data


def extract_pattern_strs(letters, smax=5):
    for ii in range(len(letters)):

        ss = letters[ii: ii + smax]
        if len(ss) < smax: break

        yield ss


def create_p_data(letters, smax=5, x=3, y=2):
    if x + y > smax: raise Exception("x,y, params err.")
    p_data = {}
    letters_list = [letters] if isinstance(letters, str) else letters
    for _letters in letters_list:
        for ss in extract_pattern_strs(_letters, smax=smax):
            xn, ym = ss[:x], ss[-y:]

            if xn not in p_data: p_data[xn] = {}
            if ym not in p_data[xn]: p_data[xn][ym] = 0

            p_data[xn][ym] += 1

    return p_data

def make_state_codes(st_df):

    st_df["state_code"] = "C"

    st_df.ix[st_df["p_change"] < -5, "state_code"] = "A"
    st_df.ix[(st_df["p_change"] < -2) & (st_df["p_change"] >= -5), "state_code"] = "B"
    st_df.ix[(st_df["p_change"] < 0) & (st_df["p_change"] >= -2), "state_code"] = "C"

    st_df.ix[(st_df["p_change"] > 0) & (st_df["p_change"] <= 2), "state_code"] = "D"
    st_df.ix[(st_df["p_change"] > 2) & (st_df["p_change"] <= 5), "state_code"] = "E"
    st_df.ix[st_df["p_change"] > 5, "state_code"] = "F"

    state_codes = []

    for index, row in st_df.iterrows():
        state_codes.append(row["state_code"])

    return "".join(state_codes)


if __name__ == '__main__':
    num_bases = {"A": -3, "B": -2, "C": -1, "D": 1, "E": 2, "F": 3}

    with open("xy_pdatas.json") as json_file:
        xy_pdatas = json.load(json_file)

    print(len(xy_pdatas))
    wps = PBB.forecast("EECCBDFC", xy_pdatas)

    score = 0

    print(wps)

    for wp in wps:
        kw, p = wp[0], wp[1]

        score += num_bases.get(kw) * p

    print(score)



