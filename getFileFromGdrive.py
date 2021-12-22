import pandas as pd
import os
import io
from datetime import datetime

from GoogleService import Folder_Search
from GoogleService import Create_Service
from googleapiclient.http import MediaIoBaseDownload

def getFiles(gdrive_path,now):
    service = Create_Service()

    folder_id = Folder_Search(service,gdrive_path)
    print("folder id= ",folder_id)

    response = service.files().list(
        q=f'mimeType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" or mimeType="application/vnd.ms-excel" and "{folder_id}" in parents',
        spaces='drive',
        fields='nextPageToken,files(id,name)',
        ).execute()

    for file in response.get('files',[]):
        
        file_id = file.get('id')
        file_name = file.get('name')
        
        if now in file_name:
            print(f"{file.get('name')} id={file.get('id')}")
            request=service.files().get_media(fileId=file_id)
            fh = io.BytesIO()
            downloader = MediaIoBaseDownload(fh, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
                print("Download %d %%." % int(status.progress() * 100))
            fname = file_name.split('T')[0]+'T'+datetime.now().strftime('%H_%M_%S')+'.xlsx'
            fh.seek(0)
            with open(f'01_INPUT_EXCEL/{now}/{fname}','wb') as  f:
                f.write(fh.read())
                f.close()




        