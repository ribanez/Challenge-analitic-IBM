import pandas as pd
from xgboost_models import *


def preOHE(df, columns_OHE, gender_str=True):
	df = pd.get_dummies(df, columns=columns_OHE)

	## Replace gender str by 0 or 1
	if gender_str:
		dict_GEN = {"GENDER":{"FEMENINO":0, "MASCULINO":1}}
		df.replace(dict_GEN, inplace=True)

	## Replace nan by 0 in all columns 
	name_col  = list(df)
	for name in name_col:
		error = df[df[name].isnull() == True]
		if len(error) > 0:
		    df[name].fillna(0, inplace=True)

	return df


def experimento1(pd_boost, diff, features):
	
	Y = pd_boost['PAYMENT_MEAN_ID'].map(lambda d: 1 if d == 1 else 0)
	X = pd_boost.drop(['PAYMENT_MEAN_ID', 'CUSTOMER_ID', 'bloqueo', 'avg_uso_tarjeta'], axis=1)

	test_size = 0.1
	X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=100)
	

	target = 'PAYMENT_MEAN_ID'

	train = X_train
	train[target] = Y_train
	test = X_test
	test[target] = Y_test

	start_time = dt.datetime.now()
	print("Start time: ",start_time)
	preds, imp, num_boost_rounds, gbm = model_max_auc(train, test, features, target, 100)	 
	print(dt.datetime.now()-start_time)

	print('\n ----TESTING WITH UNBALANCED DATA ---- \n')
	test_prediction = gbm.predict(xgb.DMatrix(diff[features],missing = -99), ntree_limit=num_boost_rounds)
	print('------ ACCURACY------')
	y_pred = np.where(test_prediction>0.5, 1, 0)
	score = accuracy_score(diff[target], y_pred, normalize = False)
	print("Accuracy (normalize = False):", score)
	score = accuracy_score(diff[target], y_pred, normalize = True)
	print("Accuracy (normalize = True):", score)


def experimento2(pd_boost, diff, features):
	
	Y = pd_boost['bloqueo'] #.map(lambda d: 1 if d == 1 else 0)
	X = pd_boost.drop(['PAYMENT_MEAN_ID', 'CUSTOMER_ID', 'bloqueo', 'avg_uso_tarjeta'], axis=1)

	test_size = 0.1
	X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=test_size, random_state=100)
	

	target = 'bloqueo'

	train = X_train
	train[target] = Y_train
	test = X_test
	test[target] = Y_test

	start_time = dt.datetime.now()
	print("Start time: ",start_time)
	preds, imp, num_boost_rounds, gbm = model_max_auc(train, test, features, target, 100)	 
	print(dt.datetime.now()-start_time)

	print('\n ----TESTING WITH UNBALANCED DATA ---- \n')
	test_prediction = gbm.predict(xgb.DMatrix(diff[features],missing = -99), ntree_limit=num_boost_rounds)
	print('------ ACCURACY------')
	y_pred = np.where(test_prediction>0.5, 1, 0)
	score = accuracy_score(diff[target], y_pred, normalize = False)
	print("Accuracy (normalize = False):", score)
	score = accuracy_score(diff[target], y_pred, normalize = True)
	print("Accuracy (normalize = True):", score)