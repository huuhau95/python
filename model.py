import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn import svm

data = pd.read_csv('DataPxK_3.csv')

data_test = data.drop(['date', 'price', 'lat', 'long', 'directionHome', 'directionBalcony', 'quarters'], axis=1)


label_investor = LabelEncoder().fit(data_test['investor'])
label_furniture = LabelEncoder().fit(data_test['furniture'])
label_district = LabelEncoder().fit(data_test['district'])

data_test['investor'] = label_investor.transform(data_test['investor'])
data_test['furniture'] = label_furniture.transform(data_test['furniture'])
data_test['district'] = label_district.transform(data_test['district'])

X = data_test.drop(['pricePerM'], axis=1)
y = data_test['pricePerM']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import DotProduct, WhiteKernel

kernel = DotProduct() + WhiteKernel()
gpr = GaussianProcessRegressor(kernel=kernel, random_state=0).fit(X_train, y_train)
print(gpr.score(X_test, y_test))

# names = ['SVR', 'SGDRegressor', 'BayesianRidge', 'LassoLars', 'ARDRegression', 'PassiveAggressiveRegressor',
#          'TheilSenRegressor', 'LinearRegression']
#
# classifiers = [
#     svm.SVR(),
#     linear_model.SGDRegressor(),
#     linear_model.BayesianRidge(),
#     linear_model.LassoLars(),
#     linear_model.ARDRegression(),
#     linear_model.PassiveAggressiveRegressor(),
#     linear_model.TheilSenRegressor(),
#     linear_model.LinearRegression()]
#
# for name, clf in zip(names, classifiers):
#     clf.fit(X_train, y_train)
#     score = clf.score(X_test, y_test)
#     print(name, score)