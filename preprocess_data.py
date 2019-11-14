#to preprocess our loaded picled streetcar data for now
import pandas as pd
import pickle
import datetime
finaldata= pd.read_pickle("processed_data/finaldata.pkl")
weatherdf=pd.read_csv("datasets/weatherstats_toronto_daily.csv")
weatherdf['date']=pd.to_datetime(weatherdf['date'])
weatherdf=weatherdf[['date','snow','avg_wind_speed','avg_visibility','avg_hourly_temperature','rain']]
weather_combined= pd.merge(finaldata,weatherdf,how='left',left_on='Report Date',right_on='date')
weather_combined.to_excel('processed_data/weatherCombined.xlsx', engine='xlsxwriter')

