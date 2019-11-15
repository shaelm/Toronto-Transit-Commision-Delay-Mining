
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth,apriori
import pandas as pd
import datetime
weatherCombineddf= pd.read_excel("weatherCombined.xlsx")
print(weatherCombineddf)

weatherCombineddf["TOD"]=""
weatherCombineddf["Wind"]=""
weatherCombineddf["TempCat"]=""
weatherCombineddf["snowCat"]=""
weatherCombineddf["rainCat"]=""
## just for TOD Cats right now
weatherCombineddf["TOD"]=weatherCombineddf[(str(weatherCombineddf['Time'])>str("06:31:00")) & (str(weatherCombineddf['Time'])<="10:31:00")]="Morning"
weatherCombineddf["TOD"]=weatherCombineddf[(str(weatherCombineddf['Time'])>str("10:31:00")) & (str(weatherCombineddf['Time'])<="3:31:00")]="Late Morning"
weatherCombineddf["TOD"]=weatherCombineddf[(str(weatherCombineddf['Time'])>str("15:31:00")) & (str(weatherCombineddf['Time'])<="18:31:00")]="After Work"
weatherCombineddf["TOD"]=weatherCombineddf[(str(weatherCombineddf['Time'])>str("18:31:00")) & (str(weatherCombineddf['Time'])<="22:31:00")]="Evening"
weatherCombineddf["TOD"]=weatherCombineddf[(str(weatherCombineddf['Time'])>str("22:31:00")) & (str(weatherCombineddf['Time'])<="06:31:00")]="Night"
## tod categories






# te=TransactionEncoder()
# te_ary = te.fit(weatherCombineddf).transform(weatherCombineddf)
# df = pd.DataFrame(te_ary, columns=te.columns_)
#
# print(fpgrowth(df, min_support=0.6, use_colnames=True))
# print(apriori(df, min_support=0.6, use_colnames=True))
#
