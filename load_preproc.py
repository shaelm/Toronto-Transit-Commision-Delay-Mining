import pandas as pd
import numpy
import pickle
years=[2014,2015,2016,2017,2018,2019]
dflist=[]
for year in years:
    file ='ttc-streetcar-delay-data-%s.xlsx'%str(year)
    df=pd.read_excel(file)
    xls=pd.ExcelFile(file)
    for sheet_name in xls.sheet_names:
        sheetdf=pd.read_excel(file,sheet_name=sheet_name)
        df=pd.concat([df,sheetdf])
    df=df.drop_duplicates()
    dflist.append(df)

finaldf=pd.concat(dflist)
finaldf.to_pickle("./finaldata.pkl")
finaldf.to_excel('finaldata.xlsx', engine='xlsxwriter')




