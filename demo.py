import pandas as pd
from datetime import datetime
from os import listdir
from os.path import isfile, join

now = datetime.now().strftime("%Y-%m-%d")
excel_path = f'01_INPUT_EXCEL/{now}/'

onlyfiles = [f for  f in listdir(excel_path) if isfile(join(excel_path,f))]

for file in onlyfiles:
    data=pd.read_excel(excel_path+file)

    print(data.head(2))
