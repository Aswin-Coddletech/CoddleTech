import os
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

def Create_Service():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first # time.
    SCOPES = ['https://www.googleapis.com/auth/drive']

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')

    if not creds or not creds.valid:    
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                    'client_secrets.json', SCOPES)
            creds = flow.run_local_server()

        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)
        return service
    
    except HttpError as error:
        # TODO(developer) - Handle errors from drive API.
        return error



def Folder_Search(service,path):
	paths=path.split('/')           # DS  , INP , CSV

	if len(paths)>1:
		parent=paths[0]             # DS
		for path in paths[1:]:
			parent=GetID(service,path,parent)   # path =INP  parent =DS

		return parent

	else:
		return GetID(service,paths[0])

def GetID(service,folder,parent=None):
	if parent==None:
		try:
			response=service.files().list(q='mimeType="application/vnd.google-apps.folder"',
		                                 spaces='drive',
		                                 fields='nextPageToken,files(id,name)',
		                                 ).execute()
		    
			for file in response.get('files',[]):
			    if file.get('name')==folder:
			        file_id=file.get('id')

			return file_id

		except:
			print('Invalid file name!!')

	else:
		try:
			response=service.files().list(q='mimeType="application/vnd.google-apps.folder"',
		                                 spaces='drive',
		                                 fields='nextPageToken,files(id,name)',
		                                 ).execute()
		    
			for file in response.get('files',[]):
			    if file.get('name')==parent or file.get('id')==parent:
			        file_id=file.get('id')

			response=service.files().list(q=f'mimeType="application/vnd.google-apps.folder" and "{file_id}" in parents',
	                                 spaces='drive',
	                                 fields='nextPageToken,files(id,name)',
	                                 ).execute()
	    
			for file in response.get('files',[]):
			    if file.get('name')==folder:
			        file_id=file.get('id')

			return file_id


		except:
			print("Invalid parent folder name file name!!")

def file_read(service,folder,mimeType,file_name):

	response=service.files().list(q=f'mimeType="{mimeType}" and "{folder}" in parents',
		spaces='drive',
		fields='nextPageToken,files(id,name)',
		).execute()

	for file in response.get('files',[]):
		if file.get('name')==file_name:
			file_id=file.get('id')


	return(file_id)