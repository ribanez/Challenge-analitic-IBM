import xgboost
import numpy as np 
import pandas as pd
import seaborn as sns
import datetime as dt
import random
import time
import matplotlib.pyplot as plt
import pprint


from xgboost.sklearn import XGBClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import average_precision_score
from sklearn import preprocessing
from sklearn.metrics import roc_curve, auc,recall_score,precision_score
from sklearn.cross_validation import cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.pipeline import make_pipeline
from sklearn.metrics import confusion_matrix

import xgboost as xgb
from xgboost import plot_tree
from xgboost import plot_importance

from operator import itemgetter
from numpy import genfromtxt



def get_importance(gbm, features):
    importance = gbm.get_fscore()
    importance = sorted(importance.items(), key=itemgetter(1), reverse=True)
    return importance


def get_features(train, test):
    trainval = list(train.columns.values)
    output = trainval
    return sorted(output)


def model_cv_simple(X, Y):
	clf = make_pipeline(StandardScaler(), XGBClassifier(nthread=1,
						n_estimators = 500,
						max_depth = 6,
						objective = 'binary:logistic'))
	start_time = dt.datetime.now()
	scores = cross_val_score(clf, X.values, Y.values, cv = 10, scoring = 'accuracy', n_jobs = 1)

	print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std()*2))
	print('Duración', dt.datetime.now()-start_time)

	clf.fit(X.values, Y.values)
	xgboost.plot_importance(clf.steps[1][1], ax=plt.gca())

	return clf


def model_max_auc(train, test, features, target, random_state=0):
    eta = 1.0
    max_depth= 6 
    subsample = 1
    colsample_bytree = 1
    min_chil_weight=1
    start_time = time.time()

    print('XGBoost params. ETA: {}, MAX_DEPTH: {}, SUBSAMPLE: {}, COLSAMPLE_BY_TREE: {}'.format(eta, max_depth, subsample, colsample_bytree))
    params = {
        "objective": "binary:logistic",
        "booster" : "gbtree",
        "eval_metric": "rmse",
        "eta": eta,
        "tree_method": 'exact',
        "max_depth": max_depth,
        "subsample": subsample,
        "colsample_bytree": colsample_bytree,
        "silent": 1,
        "min_chil_weight":min_chil_weight,
        "seed": random_state,
        #"num_class" : 22,
    }
    num_boost_round = 500
    early_stopping_rounds = 20
    test_size = 0.1

   
    
    X_train, X_valid = train_test_split(train, test_size=test_size, random_state=random_state)
    print('Length train:', X_train.shape[0])
    print('Length valid:', X_valid.shape[0])
    y_train = X_train[target]
    y_valid = X_valid[target]
    dtrain = xgb.DMatrix(X_train[features], y_train, missing=-99, feature_names=features)
    dvalid = xgb.DMatrix(X_valid[features], y_valid, missing =-99, feature_names=features)

    watchlist = [(dtrain, 'train'), (dvalid, 'eval')]
    gbm = xgb.train(params, dtrain, num_boost_round, evals=watchlist, early_stopping_rounds=early_stopping_rounds, verbose_eval=True)

    print("Validating...")
    check = gbm.predict(xgb.DMatrix(X_valid[features]), ntree_limit=gbm.best_iteration+1)
    
    #area under the precision-recall curve
    score = average_precision_score(y_valid.values, check)
    print('area under the precision-recall curve: {:.6f}'.format(score))

    
    check2=check.round()
    score = precision_score(y_valid.values, check2)
    print('precision score: {:.6f}'.format(score))

    score = recall_score(y_valid.values, check2)
    print('recall score: {:.6f}'.format(score))
    
    imp = get_importance(gbm, features)
    xgboost.plot_importance(gbm)
    print('Importance array: ', imp)

    print("Predict test set... ")
    
    
    test_prediction = gbm.predict(xgb.DMatrix(test[features],missing = -99), ntree_limit=gbm.best_iteration+1)
    score = average_precision_score(test[target].values, test_prediction)

    print('area under the precision-recall curve test set: {:.6f}'.format(score))
    
    ############################################ ROC Curve
     
    # Compute micro-average ROC curve and ROC area
    fpr, tpr, _ = roc_curve(y_valid.values, check)
    roc_auc = auc(fpr, tpr)
    plt.figure()
    lw = 2
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([-0.02, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC curve')
    plt.legend(loc="lower right")
    plt.show()


    print('Training time: {} minutes'.format(round((time.time() - start_time)/60, 2)))
    
    print('------- ACCURACY------')
    y_pred = np.where(test_prediction>0.5, 1, 0)
    score = accuracy_score(test[target], y_pred, normalize = False)
    print("Accuracy (normalize = False):", score)
    score = accuracy_score(test[target], y_pred, normalize = True)
    print("Accuracy (normalize = True):", score)
    
    return test_prediction, imp, gbm.best_iteration+1, gbm
