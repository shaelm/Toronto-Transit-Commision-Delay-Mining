import pandas as pd
import datetime
from mlxtend.frequent_patterns import fpgrowth,apriori

weatherCombineddf= pd.read_pickle("processed_data/FinalCategorizedData.pkl")

weatherCombineddf['month']=""
weatherCombineddf['year']=""
weatherCombineddf['month']=weatherCombineddf['date'].dt.month
weatherCombineddf['year']=weatherCombineddf['date'].dt.year
weatherCombineddf['Route']=weatherCombineddf['Route'].astype(str)
weatherCombineddf['Time'] = weatherCombineddf['Time'].apply(lambda dt: datetime.time(dt.hour,15*(dt.minute // 15))) # round time to 15 minutes
weatherCombineddf.dropna()
weatherCombineddf=weatherCombineddf.drop(['date','TempCat'],axis=1)

dummies = pd.get_dummies(weatherCombineddf)
dummies = dummies.drop(["Min Delay", "snow", "avg_visibility", "avg_hourly_temperature","rain","month", "year"], axis=1)

print(fpgrowth(dummies, min_support=0.4, use_colnames=True))
