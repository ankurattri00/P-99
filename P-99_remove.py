from logging import root
import os
import shutil
from sys import breakpointhook
import time

def main():
    deleted_folder_count=0
    deleted_file_count=0

    path="/PATH_TO_DELETE"
    
    days=30
    seconds = time.time() - (days * 24 * 60 * 60)
    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            if seconds >= get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                deleted_folder_count+=1
                break
            else:
                for folder in folders:
                    folder_path=os.path.join(root_folder,folder)
                    if seconds >= get_file_or_folder_age(folder_path):
                        remove_file(file_path)
                        deleted_file_count+=1
                    
        else:
            if seconds>=get_file_or_folder_age(path):
                remove_file(path)
                deleted_file_count+=1