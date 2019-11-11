#to preprocess our loaded picled streetcar data for now
import pandas as pd
import pickle
import datetime
finaldata= pd.read_pickle("./finaldata.pkl")
weatherdf=pd.read_csv("weatherstats_toronto_daily.csv")
weatherdf['date']=pd.to_datetime(weatherdf['date'])
weatherdf=weatherdf[['date','snow','avg_wind_speed']]
weather_combined= pd.merge(finaldata,weatherdf,how='left',left_on='Report Date',right_on='date')
weather_combined.to_excel('weatherCombined.xlsx', engine='xlsxwriter')

