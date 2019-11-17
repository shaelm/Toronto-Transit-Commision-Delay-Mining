import pandas as pd
import pickle
import sklearn
import datetime
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

weatherCombineddf= pd.read_pickle("processed_data/FinalCategorizedData.pkl")

weatherCombineddf['month']=""
weatherCombineddf['year']=""
weatherCombineddf['month']=weatherCombineddf['date'].dt.month
weatherCombineddf['year']=weatherCombineddf['date'].dt.year
weatherCombineddf['Route']=weatherCombineddf['Route'].astype(str)
weatherCombineddf['Time'] = weatherCombineddf['Time'].apply(lambda dt: datetime.time(dt.hour,15*(dt.minute // 15))) # round time to 15 minutes
weatherCombineddf.dropna()
train_set=weatherCombineddf[weatherCombineddf['date'].dt.year!=2019]
test_set=weatherCombineddf[weatherCombineddf['date'].dt.year==2019]
weatherCombineddf=weatherCombineddf.drop(['date','TempCat'],axis=1)
train_set=train_set.drop(['date','TempCat'],axis=1)
test_set=test_set.drop(['date','TempCat'],axis=1)

encoded_ds=pd.get_dummies(weatherCombineddf)
encoded_ds=encoded_ds.dropna()
encoded_ds_labels=encoded_ds['Min Delay']
encoded_ds_features=(encoded_ds.drop(['Min Delay'],axis=1))
train_features, test_features, train_labels, test_labels = train_test_split(encoded_ds_features, encoded_ds_labels, test_size = 0.25, random_state = 50)

feature_list=list(train_features.columns)
label_list=list(test_labels) # for baseline prediction
train_features=np.array(train_features)
train_labels=np.array(train_labels)
test_labels=np.array(test_labels)

# create a baseline of the average min delay to test against
baseline_prediction=np.array(label_list)
mean_predic=np.nanmean(baseline_prediction)
baseline_prediction.fill(mean_predic)
baseline_errors=abs(baseline_prediction-test_labels)
print("Base line error is "+str(np.nanmean(baseline_errors))+" minutes")


rf=RandomForestRegressor(n_estimators=40,random_state=50)
rf.fit(train_features,train_labels)

predictions=rf.predict(test_features)
errors=abs(predictions-test_labels)
print("Mean Prediction Error is " + str(np.mean(errors)) +" minutes")






