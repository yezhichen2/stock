# coding=utf-8

import pandas as pd
import sklearn as skl
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn import tree
from sklearn.naive_bayes import GaussianNB

import data_mgr

names = [
    "mrate5", "mrate10", "mrate_avg", "mrate_diff",
    "red_v_rate3", "red_v_rate5", "red_v_rate10",
    "rate_diff_5_10", "rate_diff_3_10", "rate_sum_5_10", "rate_sum_3_10",
    "ma10_20", "ma5_10", "ma5_20", "ma_desc", "ma_score"
]


def main1():

    all_md_df = data_mgr.get_hs300_md_features()
    X = all_md_df[names].values
    y = all_md_df['target'].values

    scaler = StandardScaler()
    X = scaler.fit_transform(X)

    # X = scaler.transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

    clf = svm.SVC(C=1.0, kernel="poly")
    clf.fit(X_train, y_train)

    print(np.mean(clf.predict(X_test) == y_test))


def main2():

    all_md_df = data_mgr.get_hs300_md_features()
    X = all_md_df[names].values
    y = all_md_df['target'].values

    #scaler = StandardScaler()
    #X = scaler.fit_transform(X)

    # X = scaler.transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

    clf = GaussianNB()
    clf.fit(X_train, y_train)

    print(np.mean(clf.predict(X_test) == y_test))

def main3():

    all_md_df = data_mgr.get_hs300_md_features()
    X = all_md_df[names].values
    y = all_md_df['target'].values

    #scaler = StandardScaler()
    #X = scaler.fit_transform(X)

    # X = scaler.transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

    clf = tree.DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    print(np.mean(clf.predict(X_test) == y_test))


if __name__ == '__main__':

    main2()