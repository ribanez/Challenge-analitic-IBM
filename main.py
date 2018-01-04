from utils import *

# Estamos dentro de los 3 primeros !

def main():
	path1 = './data/bloq2bal.csv'
	path2 = './data/unic2bal.csv'
	path3 = './data/mues2des.csv'

	bloq2bal = pd.read_csv(path1, index_col=False, header=0)
	unic2bal = pd.read_csv(path2, index_col=False, header=0)
	mues2des = pd.read_csv(path3, index_col=False, header=0)


	## ------ DESAFIO 1 -------

	input('Desafío 1 experimento 1: prediccion medio de pago ----- PRESS ENTER\n')
	pd_boost = preOHE(unic2bal, ["GSE", "CIVIL_STATUS"])
	pd2des = preOHE(mues2des, ["GSE", "CIVIL_STATUS"])
	
	ind = unic2bal.CUSTOMER_ID.isin(pd2des.CUSTOMER_ID) & pd2des.CUSTOMER_ID.isin(unic2bal.CUSTOMER_ID)
	diff = pd2des.drop(pd2des.index[ind])

	features = ['std_pago_unired', 'max_pago_unired', 'avg_pago_unired', 'pago_unired_mensual', 'avg_dia_pago_unired', 'max_dia_pago_unired', 'min_dia_pago_unired', 'avg_pago_retail_mensual', 'max_pago_retail_mensual', 'std_pago_retail_mensual', 'SPEND_AMT', 'DISCOUNT_AMT', 'GENDER', 'EDAD', 'MOBILE_CONTACTABILITY', 'EMAIL_CONTACTABILITY', 'GSE_ABC1', 'GSE_C2', 'GSE_C3', 'GSE_D', 'GSE_E', 'CIVIL_STATUS_CASADO', 'CIVIL_STATUS_DIVORCIADO', 'CIVIL_STATUS_SOLTERO', 'CIVIL_STATUS_VIUDO']
	experimento1(pd_boost, diff, features)

	input('\n Desafío 1 experimento 2: estado de morosidad ----- PRESS ENTER\n')
	pd_boost = preOHE(bloq2bal, ["GSE", "CIVIL_STATUS"])
	pd2des = preOHE(mues2des, ["GSE", "CIVIL_STATUS"])
	
	ind = unic2bal.CUSTOMER_ID.isin(pd2des.CUSTOMER_ID) & pd2des.CUSTOMER_ID.isin(unic2bal.CUSTOMER_ID)
	diff = pd2des.drop(pd2des.index[ind])

	features = ['std_pago_unired', 'max_pago_unired', 'avg_pago_unired', 'pago_unired_mensual', 'avg_dia_pago_unired', 'max_dia_pago_unired', 'min_dia_pago_unired', 'avg_pago_retail_mensual', 'max_pago_retail_mensual', 'std_pago_retail_mensual', 'SPEND_AMT', 'DISCOUNT_AMT', 'GENDER', 'EDAD', 'MOBILE_CONTACTABILITY', 'EMAIL_CONTACTABILITY', 'GSE_ABC1', 'GSE_C2', 'GSE_C3', 'GSE_D', 'GSE_E', 'CIVIL_STATUS_CASADO', 'CIVIL_STATUS_DIVORCIADO', 'CIVIL_STATUS_SOLTERO', 'CIVIL_STATUS_VIUDO']
	experimento2(pd_boost, diff, features)

	## ------ DESAFIO 2 ---------
	input('\n Desafío 2: estado de morosidad ----- PRESS ENTER\n')
	pd_boost = preOHE(bloq2bal, ["GSE", "CIVIL_STATUS"])
	pd2des = preOHE(mues2des, ["GSE", "CIVIL_STATUS"])
	
	ind = unic2bal.CUSTOMER_ID.isin(pd2des.CUSTOMER_ID) & pd2des.CUSTOMER_ID.isin(unic2bal.CUSTOMER_ID)
	diff = pd2des.drop(pd2des.index[ind])

	features = ['avg_pago_retail_mensual', 'max_pago_retail_mensual', 'std_pago_retail_mensual', 'SPEND_AMT', 'DISCOUNT_AMT', 'GENDER', 'EDAD', 'MOBILE_CONTACTABILITY', 'EMAIL_CONTACTABILITY', 'GSE_ABC1', 'GSE_C2', 'GSE_C3', 'GSE_D', 'GSE_E', 'CIVIL_STATUS_CASADO', 'CIVIL_STATUS_DIVORCIADO', 'CIVIL_STATUS_SOLTERO', 'CIVIL_STATUS_VIUDO']
	experimento2(pd_boost, diff, features)

	## ------ DESAFIO 3 ---------
	input('\n Desafío 3: uso de tarjeta unicard ----- PRESS ENTER\n')
	pd_boost = preOHE(bloq2bal, ["GSE", "CIVIL_STATUS"])
	pd2des = preOHE(mues2des, ["GSE", "CIVIL_STATUS"])
	
	ind = unic2bal.CUSTOMER_ID.isin(pd2des.CUSTOMER_ID) & pd2des.CUSTOMER_ID.isin(unic2bal.CUSTOMER_ID)
	diff = pd2des.drop(pd2des.index[ind])

	features = ['std_pago_unired', 'max_pago_unired', 'avg_pago_unired', 'pago_unired_mensual', 'avg_dia_pago_unired', 'max_dia_pago_unired', 'min_dia_pago_unired', 'GENDER', 'EDAD', 'MOBILE_CONTACTABILITY', 'EMAIL_CONTACTABILITY', 'GSE_ABC1', 'GSE_C2', 'GSE_C3', 'GSE_D', 'GSE_E', 'CIVIL_STATUS_CASADO', 'CIVIL_STATUS_DIVORCIADO', 'CIVIL_STATUS_SOLTERO', 'CIVIL_STATUS_VIUDO']
	experimento1(pd_boost, diff, features)

def main_simple_cv():
	path1 = './data/bloq2bal.csv'
	path2 = './data/unic2bal.csv'
	path3 = './data/mues2des.csv'

	bloq2bal = pd.read_csv(path1, index_col=False, header=0)
	unic2bal = pd.read_csv(path2, index_col=False, header=0)
	mues2des = pd.read_csv(path3, index_col=False, header=0)

	input('Desafío 1 experimento 1: prediccion medio de pago ----- PRESS ENTER\n')
	pd_boost = preOHE(unic2bal, ["GSE", "CIVIL_STATUS"])
	pd2des = preOHE(mues2des, ["GSE", "CIVIL_STATUS"])
	
	ind = unic2bal.CUSTOMER_ID.isin(pd2des.CUSTOMER_ID) & pd2des.CUSTOMER_ID.isin(unic2bal.CUSTOMER_ID)
	diff = pd2des.drop(pd2des.index[ind])

	features = ['std_pago_unired', 'max_pago_unired', 'avg_pago_unired', 'pago_unired_mensual', 'avg_dia_pago_unired', 'max_dia_pago_unired', 'min_dia_pago_unired', 'avg_pago_retail_mensual', 'max_pago_retail_mensual', 'std_pago_retail_mensual', 'SPEND_AMT', 'DISCOUNT_AMT', 'GENDER', 'EDAD', 'MOBILE_CONTACTABILITY', 'EMAIL_CONTACTABILITY', 'GSE_ABC1', 'GSE_C2', 'GSE_C3', 'GSE_D', 'GSE_E', 'CIVIL_STATUS_CASADO', 'CIVIL_STATUS_DIVORCIADO', 'CIVIL_STATUS_SOLTERO', 'CIVIL_STATUS_VIUDO']
	target = 'PAYMENT_MEAN_ID'

	Y = pd_boost['PAYMENT_MEAN_ID'].map(lambda d: 1 if d == 1 else 0)
	X = pd_boost.drop(['PAYMENT_MEAN_ID', 'CUSTOMER_ID', 'bloqueo', 'avg_uso_tarjeta'], axis=1)

	clf = model_cv_simple(X[features], Y)

	
	print('\n ----TESTING WITH UNBALANCED DATA ---- \n')
	test_prediction = clf.predict(diff[features])
	print('------ ACCURACY------')
	y_pred = np.where(test_prediction>0.5, 1, 0)
	score = accuracy_score(diff[target], y_pred, normalize = False)
	print("Accuracy (normalize = False):", score)
	score = accuracy_score(diff[target], y_pred, normalize = True)
	print("Accuracy (normalize = True):", score)

if __name__ == '__main__':
    	#main_simple_cv()
	main()
