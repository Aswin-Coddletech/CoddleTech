from getFileFromGdrive import getFiles
from ConverExcelToCSV import convetToCSV
from CleaningCSVFile import cleanCSV
from ConvertingToJSON import convertToJSON
from datetime import datetime
import os

# Getting Current date
now = datetime.now().strftime("%F")

# Creating folders according to current data
try:
    os.mkdir(f'01_INPUT_EXCEL/{now}')
except:
    print(f'01_INPUT_EXCEL/{now} already exist!!')

try:    
    os.mkdir(f'02_CSV-UTF8-Unclean/{now}')
except:
    print(f'02_CSV-UTF8-Unclean/{now} already exist!!')

try:
    os.mkdir(f'03_CSV-UTF8-Clean/{now}')
except:
    print(f'03_CSV-UTF8-Clean/{now} already exist!!')

try:
    os.mkdir(f'04_OUTPUT_JSON/{now}')
except:
    print(f'04_OUTPUT_JSON/{now} already exist!!')

# Creating path variables
gdrive_path = 'DataScience/10INPUT/Excel'
excel_path = f'01_INPUT_EXCEL/{now}/'
unclean_path = f'02_CSV-UTF8-Unclean/{now}/'
clean_path = f'03_CSV-UTF8-Clean/{now}/'
json_path = f'04_OUTPUT_JSON/{now}/'

# Downloading excel file from gdrive
getFiles(gdrive_path,now)

# Converting the downloaded excel file into csv-utf8 and store it in 02_CSV-UTF8-Unclean folder
convetToCSV(excel_path,unclean_path)

# Saving cleaned csv file from unclean csv file
cleanCSV(unclean_path,clean_path)

# Converting clean csv to JSON
convertToJSON(clean_path,json_path)



