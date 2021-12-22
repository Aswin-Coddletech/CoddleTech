import pandas as pd
from os import listdir
from os.path import isfile, join
from datetime import datetime

def convetToCSV(input_path,output_path):
    # Getting all excel files inside Excel folder and store it in onlyfiles
    onlyfiles = [f for  f in listdir(input_path) if isfile(join(input_path,f))]
    print(onlyfiles)
    print('Excel path = ',input_path)
    for file in onlyfiles:
        print('File name = ',file)
        print(input_path+file)
        # Reading excel files from Excel folder and removing unwanted columns
        data = pd.read_excel(input_path+file)
        fname = file.split('T')[0]+'T'+datetime.now().strftime('%H_%M_%S')
        # Converting excel file into csv and encoding to utf-8 format
        data.to_csv(output_path+fname+'.csv',index=False,encoding='utf-8')