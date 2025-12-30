import os
import shutil
import datetime
import schedule
import time

scource_dir = "C:\\Users\\Utente\\Pictures"
destination_dir = "C:\\Users\\Utente\\Desktop\\Backups"

def copy_folder_to_directory(source,dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))
    try:
        shutil.copytree(source, dest_dir)
        print(f"Backup successful: {dest_dir}")
    except Exception as e:
        print(f"Error during backup: {e}")
schedule.every().day.at("16:06").do(lambda: copy_folder_to_directory(scource_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)
