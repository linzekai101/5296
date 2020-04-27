import pandas as pd
import numpy as np
import time


#read the data
train = pd.read_csv('train.csv', delimiter='\t')
train.Date=pd.to_datetime(train.Date,unit='s')
test = pd.read_csv('test.csv', delimiter='\t')
test.Date=pd.to_datetime(test.Date,unit='s')

#Change the header
train.rename(columns={'Unnamed: 0':'No','Day of Week':'DayofWeek'},inplace=True) 
test.rename(columns={'Unnamed: 0':'No','Day of Week':'DayofWeek'},inplace=True) 
train.Date = train.Date.dt.hour
train.rename(columns={'Date':'Hour'},inplace=True) 

#lable the category
from sklearn import preprocessing
label = preprocessing.LabelEncoder()
crime = label.fit_transform(train.Category)
crime_test = label.fit_transform(test.Category)

# train data binary processing 
district = pd.get_dummies(train.PdDistrict)
days = pd.get_dummies(train.DayofWeek)
hour = pd.get_dummies(train.Hour)
train_data = pd.concat([hour, district, days], axis=1)  
#label col
train_data['crime'] = crime 


# test data binary processing 
district = pd.get_dummies(test.PdDistrict)
days = pd.get_dummies(test.DayofWeek)
hour = pd.get_dummies(test.Date.dt.hour)
test_data = pd.concat([hour, district, days], axis=1)  
test_data['crime'] = crime_test


#divide samples into training sets and validation sets 
from sklearn.model_selection import train_test_split
training, validation = train_test_split(train_data, train_size=0.7)



#Naive bayes
from sklearn.metrics import log_loss
from sklearn.naive_bayes import BernoulliNB



#train the model
model = BernoulliNB()
feature_list = training.columns.tolist()   
feature_list = feature_list[:len(feature_list) - 1]  

for i in range(20):
    t1 = time.time()#record the start time 
    model.fit(training[feature_list], training['crime'])   
    t2=time.time()
    print(t2-t1)

