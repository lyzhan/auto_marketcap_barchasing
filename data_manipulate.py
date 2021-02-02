import pandas as pd
from datetime import datetime
from pathlib import Path

pathlist = Path('.').glob('*.txt')
for path in pathlist:
    # because path is object not string
    path_in_str = str(path)
    df=pd.read_table(path_in_str,header=None,names=['index','d','m'])
    df['m']=df['m']/10000.0
    df['date_time']=df['d'].apply(datetime.fromtimestamp)
