# import dependencies
import os
import shutil
from datetime import datetime




# get download file
# download folder path and destination folder path
download_folder_path = r'C:\Users\mfmohammad\Downloads'
destination_folder_path = r'C:\Users\mfmohammad\OneDrive - UNICEF\Desktop\Data Cleaning'

# list of file name to move
file_to_move = ['Donor With Invalid Email', 'Donor With Invalid IC', 
                'Donor With Invalid Phone Number', 'Donor Without Age and Birthdate', 
                'Donor Without Ethnic', 'Donor Without Gender'
                ]

# create folder 
# get the current date and month
current_date = datetime.now()
short_date_and_month = current_date.strftime("%d %b")
short_month = current_date.strftime("%b")

# create destination path
destination_path = os.path.join(destination_folder_path, short_month, short_date_and_month )

# move file

print(short_date_and_month)
print(short_month)
print('code successfully run')