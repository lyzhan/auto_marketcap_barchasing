import numpy as np
import datetime as dt
import pandas as pd
from datetime import datetime
from pathlib import Path

start=dt.datetime(2010,7,1,0,0,0)
end=dt.datetime(2021,2,1,0,0,0)
timelist=pd.date_range(start, end,freq='1MS')
pathlist = Path('.').glob('*.txt')
df_dump=pd.DataFrame(columns=timelist)
for path in pathlist:
    # because path is object not string
    path_in_str = str(path)
    df=pd.read_table(path_in_str,header=None,names=['index','d','m'])
    df['m']=df['m']/10000.0
    df['date_time']=df['d'].apply(datetime.fromtimestamp)
