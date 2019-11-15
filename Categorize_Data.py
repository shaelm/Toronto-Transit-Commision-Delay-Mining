
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth,apriori
import pandas as pd
import datetime
weatherCombineddf= pd.read_pickle("processed_data/weatherCombined.pkl")

weatherCombineddf["TOD"]=""
weatherCombineddf["delayCat"]=""
weatherCombineddf["visCat"]=""
weatherCombineddf["dirCat"]=""
weatherCombineddf["Wind"]=""
weatherCombineddf["TempCat"]=""
weatherCombineddf["Month"]=""
weatherCombineddf["snowCat"]=""
weatherCombineddf["rainCat"]=""
## just for TOD Cats right now
weatherCombineddf.loc[(weatherCombineddf['Time'].astype(str)>"06:31:00") & (weatherCombineddf['Time'].astype(str)<="10:31:00"),"TOD"]="Morning"
weatherCombineddf.loc[(weatherCombineddf['Time'].astype(str)>"10:31:00") & (weatherCombineddf['Time'].astype(str)<="15:31:00"),"TOD"]="Late Morning"
weatherCombineddf.loc[(weatherCombineddf['Time'].astype(str)>"15:31:00") & (weatherCombineddf['Time'].astype(str)<="18:31:00"),"TOD"]="After Work"
weatherCombineddf.loc[(weatherCombineddf['Time'].astype(str)>"18:31:00") & (weatherCombineddf['Time'].astype(str)<="22:31:00"),"TOD"]="Evening"
weatherCombineddf.loc[(weatherCombineddf['Time'].astype(str)>"22:31:00") | (weatherCombineddf['Time'].astype(str)<="06:31:00"),"TOD"]="Night"

##Month Cats
weatherCombineddf.loc[(weatherCombineddf['Report Date'].dt.month==1),"Month"]="Jan"
weatherCombineddf.loc[(weatherCombineddf['Report Date'].dt.month==2),"Month"]="Feb"
weatherCombineddf.loc[(weatherCombineddf['Report Date'].dt.month==3),"Month"]="Mar"
weatherCombineddf.loc[(weatherCombineddf['Report Date'].dt.month==4),"Month"]="Apr"
weatherCombineddf.loc[(weatherCombineddf['Report Date'].dt.month==5),"Month"]="May"
weatherCombineddf.loc[(weatherCombineddf['Report Date'].dt.month==6),"Month"]="Jun"
weatherCombineddf.loc[(weatherCombineddf['Report Date'].dt.month==7),"Month"]="Jul"
weatherCombineddf.loc[(weatherCombineddf['Report Date'].dt.month==8),"Month"]="Aug"
weatherCombineddf.loc[(weatherCombineddf['Report Date'].dt.month==9),"Month"]="Sep"
weatherCombineddf.loc[(weatherCombineddf['Report Date'].dt.month==10),"Month"]="Oct"
weatherCombineddf.loc[(weatherCombineddf['Report Date'].dt.month==11),"Month"]="Nov"
weatherCombineddf.loc[(weatherCombineddf['Report Date'].dt.month==12),"Month"]="Dec"



## tod categories
##wind cats
weatherCombineddf.loc[(weatherCombineddf['avg_wind_speed'].astype(float)>=0) & (weatherCombineddf['avg_wind_speed'].astype(float)<=10),"Wind"]="No-Light Wind"
weatherCombineddf.loc[(weatherCombineddf['avg_wind_speed'].astype(float)>10) & (weatherCombineddf['avg_wind_speed'].astype(float)<=20),"Wind"]="Light-Medium Wind"
weatherCombineddf.loc[(weatherCombineddf['avg_wind_speed'].astype(float)>20) & (weatherCombineddf['avg_wind_speed'].astype(float)<=30),"Wind"]="Medium-Heavy Wind"
weatherCombineddf.loc[(weatherCombineddf['avg_wind_speed'].astype(float)>30) & (weatherCombineddf['avg_wind_speed'].astype(float)<=50),"Wind"]="Heavy Wind"
weatherCombineddf.loc[(weatherCombineddf['avg_wind_speed'].astype(float)>50),"Wind"]="Extremely Heavy Wind"


##Delay Cats, over an hr is an extreme delay
weatherCombineddf.loc[(weatherCombineddf['Min Delay'].astype(float)>=0) & (weatherCombineddf['Min Delay'].astype(float)<=50),"delayCat"]="No-Light Delay"
weatherCombineddf.loc[(weatherCombineddf['Min Delay'].astype(float)>5) & (weatherCombineddf['Min Delay'].astype(float)<=15),"delayCat"]="Light-Medium Delay"
weatherCombineddf.loc[(weatherCombineddf['Min Delay'].astype(float)>15) & (weatherCombineddf['Min Delay'].astype(float)<=30),"delayCat"]="Medium-Heavy Delay"
weatherCombineddf.loc[(weatherCombineddf['Min Delay'].astype(float)>30) & (weatherCombineddf['Min Delay'].astype(float)<=50),"delayCat"]="Heavy Delay"
weatherCombineddf.loc[(weatherCombineddf['Min Delay'].astype(float)>60),"delayCat"]="Extreme Delay"

##Direction Categories
weatherCombineddf.loc[(weatherCombineddf['Direction'].str.contains("N",regex=False,na=False)) ,"dirCat"]="North"
weatherCombineddf.loc[(weatherCombineddf['Direction'].str.contains("S",regex=False,na=False)) ,"dirCat"]="South"
weatherCombineddf.loc[(weatherCombineddf['Direction'].str.contains("E",regex=False,na=False)) ,"dirCat"]="East"
weatherCombineddf.loc[(weatherCombineddf['Direction'].str.contains("W",regex=False,na=False)) ,"dirCat"]="West"
##Temp Categories
weatherCombineddf.loc[(weatherCombineddf['avg_hourly_temperature'].astype(float)>20) & (weatherCombineddf['avg_hourly_temperature'].astype(float)<=30),"tempCat"]="20:30 C"
weatherCombineddf.loc[(weatherCombineddf['avg_hourly_temperature'].astype(float)>30) ,"tempCat"]=">30 C"
weatherCombineddf.loc[(weatherCombineddf['avg_hourly_temperature'].astype(float)>10) & (weatherCombineddf['avg_hourly_temperature'].astype(float)<=15),"tempCat"]="10:15 C"
weatherCombineddf.loc[(weatherCombineddf['avg_hourly_temperature'].astype(float)>15) & (weatherCombineddf['avg_hourly_temperature'].astype(float)<=20),"tempCat"]="15:20 C"
weatherCombineddf.loc[(weatherCombineddf['avg_hourly_temperature'].astype(float)>10) & (weatherCombineddf['avg_hourly_temperature'].astype(float)<=15),"tempCat"]="10:15 C"
weatherCombineddf.loc[(weatherCombineddf['avg_hourly_temperature'].astype(float)>5) & (weatherCombineddf['avg_hourly_temperature'].astype(float)<=10),"tempCat"]="0:10 C"
weatherCombineddf.loc[(weatherCombineddf['avg_hourly_temperature'].astype(float)>0) & (weatherCombineddf['avg_hourly_temperature'].astype(float)<=5),"tempCat"]="0:5C"
weatherCombineddf.loc[(weatherCombineddf['avg_hourly_temperature'].astype(float)>-5) & (weatherCombineddf['avg_hourly_temperature'].astype(float)<=0),"tempCat"]="-5:0 C"
weatherCombineddf.loc[(weatherCombineddf['avg_hourly_temperature'].astype(float)>-10) & (weatherCombineddf['avg_hourly_temperature'].astype(float)<=-5),"tempCat"]="-10:-5 C"
weatherCombineddf.loc[(weatherCombineddf['avg_hourly_temperature'].astype(float)>-15) & (weatherCombineddf['avg_hourly_temperature'].astype(float)<=-10),"tempCat"]="-15:-10 C"
weatherCombineddf.loc[(weatherCombineddf['avg_hourly_temperature'].astype(float)>-20.0) & (weatherCombineddf['avg_hourly_temperature'].astype(float)<=-15),"tempCat"]="-20:-15 C"
weatherCombineddf.loc[(weatherCombineddf['avg_hourly_temperature'].astype(float)>-25) & (weatherCombineddf['avg_hourly_temperature'].astype(float)<=-20),"tempCat"]="-25:-20 C"
weatherCombineddf.loc[(weatherCombineddf['avg_hourly_temperature'].astype(float)>-30) & (weatherCombineddf['avg_hourly_temperature'].astype(float)<=-25),"tempCat"]="-30:-25 C"
weatherCombineddf.loc[(weatherCombineddf['avg_hourly_temperature'].astype(float)<-30) ,"tempCat"]="<-30 C"

##Rain Cats
weatherCombineddf.loc[(weatherCombineddf['rain'].astype(float)>=0) & (weatherCombineddf['rain'].astype(float)<=5),"rainCat"]="0-5 mm Rain"
weatherCombineddf.loc[(weatherCombineddf['rain'].astype(float)>5) & (weatherCombineddf['rain'].astype(float)<=10),"rainCat"]="5-10 mm Rain"
weatherCombineddf.loc[(weatherCombineddf['rain'].astype(float)>10) & (weatherCombineddf['rain'].astype(float)<=15),"rainCat"]="10-15 mm Rain"
weatherCombineddf.loc[(weatherCombineddf['rain'].astype(float)>15) & (weatherCombineddf['rain'].astype(float)<=20),"rainCat"]="15-20 mm Rain"
weatherCombineddf.loc[(weatherCombineddf['rain'].astype(float)>20) & (weatherCombineddf['rain'].astype(float)<=25),"rainCat"]="20-25 mm Rain"
weatherCombineddf.loc[(weatherCombineddf['rain'].astype(float)>25) & (weatherCombineddf['rain'].astype(float)<=30),"rainCat"]="25-30 mm Light Rain"
weatherCombineddf.loc[(weatherCombineddf['rain'].astype(float)>30) ,"rainCat"]=">30 mm Rain"
##Snow Cats
weatherCombineddf.loc[(weatherCombineddf['snow'].astype(float)>=0) & (weatherCombineddf['snow'].astype(float)<=2),"snowCat"]="0-2 cm Snow"
weatherCombineddf.loc[(weatherCombineddf['snow'].astype(float)>2) & (weatherCombineddf['snow'].astype(float)<=5),"snowCat"]="2-5 cm Snow"
weatherCombineddf.loc[(weatherCombineddf['snow'].astype(float)>5) & (weatherCombineddf['snow'].astype(float)<=8),"snowCat"]="5-8 cm Snow"
weatherCombineddf.loc[(weatherCombineddf['snow'].astype(float)>8) & (weatherCombineddf['snow'].astype(float)<=11),"snowCat"]="8-11 cm Snow"
weatherCombineddf.loc[(weatherCombineddf['snow'].astype(float)>11) & (weatherCombineddf['snow'].astype(float)<=14),"snowCat"]="11-14 cm Snow"
weatherCombineddf.loc[(weatherCombineddf['snow'].astype(float)>14) & (weatherCombineddf['snow'].astype(float)<=17),"snowCat"]="14-17 cm Snow"
weatherCombineddf.loc[(weatherCombineddf['snow'].astype(float)>17) & (weatherCombineddf['snow'].astype(float)<=20),"snowCat"]="17-20 cm Snow"
weatherCombineddf.loc[(weatherCombineddf['snow'].astype(float)>20) & (weatherCombineddf['snow'].astype(float)<=25),"snowCat"]="20-25 cm Snow"
weatherCombineddf.loc[(weatherCombineddf['snow'].astype(float)>25) ,"snowCat"]=">25 cm Snow"
##Visibility Categories
weatherCombineddf.loc[(weatherCombineddf['avg_visibility'].astype(float)>0) & (weatherCombineddf['avg_visibility'].astype(float)<=10000),"visCat"]="Very Poor Visibility"
weatherCombineddf.loc[(weatherCombineddf['avg_visibility'].astype(float)>10000) & (weatherCombineddf['avg_visibility'].astype(float)<=20000),"visCat"]="Poor Visibility"
weatherCombineddf.loc[(weatherCombineddf['avg_visibility'].astype(float)>20000) & (weatherCombineddf['avg_visibility'].astype(float)<=30000),"visCat"]="Okay Visibility"
weatherCombineddf.loc[(weatherCombineddf['avg_visibility'].astype(float)>30000) ,"visCat"]="Good Visibility"
#Drop bad and uncategorized columns
weatherCombineddf=weatherCombineddf.drop(['Location'],axis=1)
weatherCombineddf=weatherCombineddf.drop(['Direction'],axis=1)
weatherCombineddf=weatherCombineddf.drop(['Delay'],axis=1)
weatherCombineddf=weatherCombineddf.drop(['Gap'],axis=1)
weatherCombineddf=weatherCombineddf.drop(['Min Gap'],axis=1)
weatherCombineddf=weatherCombineddf.drop(['date'],axis=1)
weatherCombineddf=weatherCombineddf.drop(['snow'],axis=1)
weatherCombineddf=weatherCombineddf.drop(['rain'],axis=1)
weatherCombineddf=weatherCombineddf.drop(['avg_wind_speed'],axis=1)
weatherCombineddf=weatherCombineddf.drop(['avg_hourly_temperature'],axis=1)
weatherCombineddf=weatherCombineddf.drop(['avg_visibility'],axis=1)
weatherCombineddf=weatherCombineddf.drop(['Vehicle'],axis=1)
weatherCombineddf=weatherCombineddf.drop(['Time'],axis=1)
weatherCombineddf=weatherCombineddf.drop(['Report Date'],axis=1)
weatherCombineddf=weatherCombineddf.drop(['Incident ID'],axis=1)

weatherCombineddf.to_excel('processed_data/FinalCategorizedData.xlsx', engine='xlsxwriter')
weatherCombineddf.to_pickle("processed_data/FinalCategorizedData.pkl")

