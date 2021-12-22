import os
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

def Create_Service():
	secret_file='client_secret1.json'
	scope='https://www.googleapis.com/auth/drive'
	flow=InstalledAppFlow.from_client_secrets_file(secret_file,scope)
	cred=flow.run_local_server()

	service=build('drive','v3',credentials=cred)

	return service

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