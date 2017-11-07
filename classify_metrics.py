#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 17:52:14 2017

@author: wanda
"""
from sklearn.metrics import fbeta_score, make_scorer
from sklearn.metrics import confusion_matrix


#https://en.wikipedia.org/wiki/F1_score

def fnr_score(y, y_pred):
    cm = confusion_matrix(y, y_pred)
    tp = cm[1][1]*1.
    fn = cm[1][0]*1.
    fnr = fn/(tp+fn)
    return fnr

def fpr_score(y, y_pred):
    cm = confusion_matrix(y, y_pred)
    tn = cm[0][0]*1.
    fp = cm[0][1]*1.
    fpr = fp/(tn+fp)
    return fpr

def for_score(y, y_pred):
    #false omission rate
    cm = confusion_matrix(y, y_pred)
    fn = cm[1][0]*1.
    tn = cm[0][0]*1.
    fpr = fn/(tn+fn)
    return fpr

fnr_scorer = make_scorer(fnr_score)
fpr_scorer = make_scorer(fpr_score)
for_scorer = make_scorer(for_score)
f2_scorer = make_scorer(fbeta_score, beta=2)