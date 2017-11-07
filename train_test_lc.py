#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 17:59:38 2017

@author: wanda
"""
import numpy as np 
from sklearn.model_selection import train_test_split
from random import randint
import matplotlib.pyplot as plt 
from classify_metrics import *

def learning_curve_scores(clf,X_train,y_train, X_test,y_test, score,train_sizes = np.linspace(.1, 1.0, 5),beta=None):
    #Scores for a model when experience increases.
    lc_score_train, lc_score_test = [], []
    for size in train_sizes:
        # Get random section from train data, stratified.
        if size!=1.0:
            X_t,__, y_t, __ = train_test_split(X_train, y_train, train_size=size, random_state=randint(1,100), stratify= y_train)
        else:
            X_t, y_t = X_train, y_train  
            
        # Fit with train
        clf.fit(X_t,y_t)
        # Predict on Train
        y_pred_train = clf.predict(X_t)
        # Predict on Test
        y_pred_test = clf.predict(X_test)
        # Save scores
        if beta!= None:
            lc_score_train.append(score(y_t, y_pred_train,beta))
            lc_score_test.append(score(y_test, y_pred_test,beta))     
        else:
            lc_score_train.append(score(y_t, y_pred_train))
            lc_score_test.append(score(y_test, y_pred_test))     
    
    return lc_score_train, lc_score_test



def plot_lc(title, scores):
    metrics = ['ACC','TPR','FPR','FNR','PRE','F2']
    for metric in metrics:
        plt.figure()
        plt.title(title+" "+metric)
        plt.xlabel("Training examples")
        plt.ylabel("Score")
        train_sizes = np.linspace(.1, 1.0, 5)
        train_scores_mean = np.mean(np.array(scores[metric+'_train']),axis=0)
        train_scores_std =np.std(np.array(scores[metric+'_train']),axis=0)
        test_scores_mean = np.mean(np.array(scores[metric+'_test']),axis=0)
        test_scores_std = np.std(np.array(scores[metric+'_test']),axis=0)
        plt.grid()

        plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                         train_scores_mean + train_scores_std, alpha=0.1,
                         color="r")
        plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                         test_scores_mean + test_scores_std, alpha=0.1, color="g")
        plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
                 label="Training score")
        plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
                 label="Test score")#label="Cross-validation score"

        plt.legend(loc="best")
    return plt