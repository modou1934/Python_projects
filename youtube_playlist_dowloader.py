from pytubefix import Playlist
from pytubefix.cli import on_progress
import tkinter as tk
from tkinter import filedialog



def download_video(url, save_path):
    try:
        pl = Playlist(url)
        for video in pl.videos:
            ys = video.streams.get_highest_resolution()
            ys.download(output_path=save_path)
    except Exception as e:
        print(f"Error: {e}")


def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        return folder
    else:
        print("No folder selected.")
        return None



if  __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    video_url = input("Enter url: ")
    save_dir = open_file_dialog()
    if save_dir == None:
        print("No directory selected. Exiting.")
        exit()

    print(f"Downloading video from: {video_url}")
    print(f"Saving to: {save_dir}")
    download_video(video_url, save_dir)