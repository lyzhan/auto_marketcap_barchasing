import pandas as pd
from datetime import datetime

df=pd.read_table('Tesla.txt',header=None,names=['index','d','m'])
df['m']=df['m']/10000.0
df['date_time']=df['d'].apply(datetime.fromtimestamp)
print(df)