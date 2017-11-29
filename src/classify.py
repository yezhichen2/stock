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

    from sklearn.model_selection import GridSearchCV
    from sklearn import svm

    model = svm.SVC(kernel="rbf")

    param_grid = {"C": [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100, 300, 1000], "gamma": [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100, 300, 1000]}

    clf = GridSearchCV(model, param_grid=param_grid,
                       cv=5, scoring='accuracy')

    clf.fit(X_train, y_train)

    model = clf.best_estimator_

    print(clf.best_params_)
    print(np.mean(model.predict(X_test) == y_test))


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

    main1()