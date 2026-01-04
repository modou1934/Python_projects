import os
import re
import shutil
import time
from collections import deque
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path

class DownloadHandler(FileSystemEventHandler):
    def __init__(self):
        self.recent_events = deque(maxlen=100)  # Evita loop

    def on_created(self, event):
        self.process_event(event)

    def on_modified(self, event):  # Per download lenti
        if not event.is_directory:
            time.sleep(1)  # Breve delay
            self.process_event(event)

    def process_event(self, event):
        src_path = Path(event.src_path)
        if src_path.is_directory or src_path.name.startswith('.'):  # Ignora dir e nascosti
            return

        # Ignora temporanei browser
        if src_path.suffix.lower() in ['.crdownload', '.tmp', '.part', '.download']:
            return

        img_ext = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg']
        if src_path.suffix.lower() in img_ext:
            print(f"📄 Immagine rilevata: {src_path.name}")
            dest_folder = Path(folder_to_watch) / "Immagini"
            dest_folder.mkdir(exist_ok=True)

            dest_path = dest_folder / src_path.name
            if dest_path.exists():
                stem = src_path.stem
                dest_path = dest_folder / f"{stem}_{int(time.time())}.jpg"  # Duplicati

            try:
                shutil.move(src_path, dest_path)  # Solo move!
                print(f"✅ Spostato: {dest_path}")
            except Exception as e:
                print(f"❌ Errore: {e}")

# Config
folder_to_watch = Path.home() / "Downloads"

event_handler = DownloadHandler()
observer = Observer()
observer.schedule(event_handler, str(folder_to_watch), recursive=False)
observer.start()

print(f"🔍 Monitoraggio: {folder_to_watch}")
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()
