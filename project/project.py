import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

excelfile = pd.ExcelFile(r'C:\Users\ab522tx\Desktop\assgnmnts\project\TakenMind-Python-Analytics-Problem-case-study-1-1.xlsx')
df1 = excelfile.parse('Existing employees')
# print(df1.head())
df2 = excelfile.parse('Employees who have left')
# print(df2.head())
# df1.drop('Emp ID',inplace=True,axis=1)
# df2.drop('Emp ID',inplace=True,axis=1)
df1['Existing'] = 1
df2['Existing'] = 0
# print(df1.info(),df2.info())
# print(df1.head())
# print(df2.head())
dataframe = df1.append(df2)
# print(dataframe.info())
# print(dataframe.salary.value_counts())
# print(dataframe.dept.value_counts())
# print(dataframe.sample(20))
print(dataframe.info())

# cat_types = dataframe.select_dtypes('object')
# # int_types = dataframe.select_dtypes('int64')
# float_types = dataframe.select_dtypes('float')
# print(cat_types)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
dataframe['dept'] = le.fit_transform(dataframe.dept)
dataframe['salary'] = le.fit_transform(dataframe.salary)
print(dataframe.corr(method='pearson')['Existing'])
# print(dataframe.Salary.value_counts())
# print(dataframe.info())
feature_data = dataframe[['Emp ID','satisfaction_level','last_evaluation','number_project','average_montly_hours','time_spend_company','Work_accident','promotion_last_5years','dept','salary']]
target_data = dataframe['Existing']
# print(target_data.sample(20))
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(feature_data,target_data,test_size=0.5)
# print(x_train,y_train)
from sklearn.linear_model import LinearRegression,LogisticRegression
# lg = LinearRegression()
# lg.fit(x_train,y_train)
# lg.predict(x_test)
# print(lg.score(x_test,y_test))
lr = LogisticRegression()
lr.fit(x_train,y_train)
pred = lr.predict(x_test)
print(lr.score(x_test,y_test))
from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor
dtc = DecisionTreeClassifier()
dtc.fit(x_train,y_train)
y_pred = dtc.predict(x_test)
print(dtc.score(x_test,y_test))
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))
dtr = DecisionTreeRegressor()
dtr.fit(x_train,y_train)
y_pred1 = dtr.predict(x_test)
print(dtr.score(x_test,y_test))
print(confusion_matrix(y_test,y_pred1))
