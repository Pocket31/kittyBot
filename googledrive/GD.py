from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
import io
import pprint
from googleapiclient.discovery import build
from google.oauth2 import service_account

pp = pprint.PrettyPrinter(indent=4)

SCOPES = ['https://www.googleapis.com/auth/drive']

SERVICE_ACCOUNT_FILE = 'C:/Users/cr796/OneDrive/Документы/kittyBot/shop-402114-a6896552ca04.json'

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)
# results = service.files().list().execute()
# pp.pprint(results)
results = service.files().list(q="mimeType='text/plain'").execute()


def check_product():
    return len(results['files'])


def download_file():
    file_id = results['files'][0]['id']
    request = service.files().get_media(fileId=file_id)
    filename = 'C:/Users/cr796/OneDrive/Документы/kittyBot/file.txt'
    fh = io.FileIO(filename, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))

# pp.pprint(check_product())


def move_file():
    file_id = results['files'][0]['id']
    folder_id = '1NYfQzHrq_xecGEr2_4o9bXqeoKwFItrG'

    if not file_id or not folder_id:
        raise Exception(f'Did not find file specefied')

    # Retrieve the existing parents to remove
    file = service.files().get(fileId=file_id, fields='parents').execute()
    previous_parents = ",".join(file.get('parents'))

    # Move the file to the new folder
    file = service.files().update(
        fileId=file_id,
        addParents=folder_id,
        removeParents=previous_parents,
        fields='id, parents'
    ).execute()


move_file()
