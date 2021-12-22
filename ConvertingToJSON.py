import pandas as pd
from os import listdir
from os.path import isfile, join
from datetime import datetime

def convertToJSON(input_path,output_path):
    # Getting all files inside CSV-UTF8-Clean folder
    cleanfiles = [f for f in listdir(input_path) if isfile(join(input_path,f))]

    for file in cleanfiles:
        # Reading clean file 
        data = pd.read_csv(input_path+file)

        fname = file.split('T')[0]+'T'+datetime.now().strftime('%H_%M_%S')
        # Saving the csv file in json format and store inside JSON folder
        data.to_json(output_path+fname+'.json',orient='records')