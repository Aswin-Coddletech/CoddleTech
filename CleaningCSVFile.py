import pandas as pd
import numpy as np
from os import listdir
from os.path import isfile, join
from datetime import datetime

def cleanCSV(input_path,output_path):
    # Getting all Unclean files from CSV-UTF8-Unclean folder
    uncleanfiles = [f for f in listdir(input_path) if isfile(join(input_path,f))]

    for file in uncleanfiles:
        # Reading csv-utf8 unclean files
        data = pd.read_csv(input_path+file)

        # Replacing string 'na' with NaN 
        data.replace('na',np.nan,inplace=True)
        
        # Removing Columns having 100% null values
        data.dropna(axis=1,thresh=1,inplace=True)

        fname = file.split('T')[0]+'T'+datetime.now().strftime('%H_%M_%S')+'.csv'
        # Saving the csv file to CSV-UTF8-Clean folder
        data.to_csv(output_path+fname,index=False)