import numpy as np
import datetime as dt
import pandas as pd
from datetime import datetime
from pathlib import Path

start=dt.datetime(2010,7,1,0,0,0)
end=dt.datetime(2021,2,1,0,0,0)
timedf=pd.date_range(start, end,freq='1MS')
pathlist = Path('.').glob('*.txt')
# df_dump=pd.DataFrame(columns=timedf)
data_dump=[]
namelist=[]
timelist=timedf.to_list()
for path in pathlist:
    # because path is object not string
    path_in_str = str(path)
    namelist.append(path_in_str)
    df=pd.read_table(path_in_str,header=None,names=['index','d','m'])
    df.drop('index',axis=1,inplace=True)
    df.drop_duplicates(subset=['d'],inplace=True)
    df['m']=df['m']/10000.0
    df.set_index(df['d'].apply(datetime.fromtimestamp),inplace=True)
    df.drop('d',axis=1,inplace=True)
    monthlydata=np.zeros(len(timelist))
    for tm in timelist:
        try:
            monthlydata[timelist.index(tm)]=df.iloc[df.index.get_loc(tm,method='nearest',tolerance=dt.timedelta(days=31))]['m']
        except:
            pass# print('Missing at '+tm.strftime('%Y%M')+' for '+path_in_str)
    data_dump.append(monthlydata)

df_dump=pd.DataFrame(data_dump,columns=timedf)
df_dump.set_index([pd.Index(namelist)],inplace=True)
df_dump.to_csv('auto_marketcap_'+start.strftime('%Y%M')+'_'+end.strftime('%Y%M')+'.csv')