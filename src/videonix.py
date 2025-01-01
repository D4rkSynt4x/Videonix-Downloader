import os
import threading
import sys
from tkinter import Tk, Label, Entry, Button, StringVar, filedialog, messagebox, ttk

from yt_dlp import YoutubeDL

# Path to the FFmpeg binary
FFMPEG_PATH = "C:\\Users\\Moshin\\OneDrive\\Desktop\\videonix\\ffmpeg\\bin\\ffmpeg.exe"

# Adding control variables for Stop and Pause functionality
abort_flag = threading.Event()
pause_flag = threading.Event()

# Redirect technical logs to a file
log_file = open("videonix_log.txt", "w")
sys.stdout = log_file
sys.stderr = log_file

# Function to validate paths
def validate_paths():
    if not os.path.exists(FFMPEG_PATH):
        messagebox.showerror("Error", "FFmpeg not found. Please ensure it is correctly configured.")
        return False
    return True

# The progress bar
def progress_hook(d):
    if d['status'] == 'downloading':
        progress_percentage = float(d['_percent_str'].strip('%'))
        progress_var.set(progress_percentage)
    elif d['status'] == 'finished':
        progress_var.set(100)
        messagebox.showinfo("Download Complete", "The video has been successfully downloaded!")

# Stop the download
def stop_download():
    abort_flag.set()
    messagebox.showinfo("Stopped", "The download has been stopped.")

# Pause and Resume the download
def toggle_pause():
    if not pause_flag.is_set():
        pause_flag.set()
        pause_button.config(text="Resume", bg="green")
        messagebox.showinfo("Paused", "The download has been paused.")
    else:
        pause_flag.clear()
        pause_button.config(text="Pause", bg="green")
        messagebox.showinfo("Resumed", "The download has resumed.")

# Download function
def download_video():
    if not validate_paths():
        return

    url = url_var.get()
    save_path = folder_var.get()

    if not url:
        messagebox.showerror("Error", "Please paste a valid URL!")
        return
    if not save_path:
        messagebox.showerror("Error", "Please select a storage folder!")
        return

    # yt-dlp options
    ydl_opts = {
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
        'progress_hooks': [progress_hook],
        'merge_output_format': 'mp4',  # Ensures the final file is in MP4 format
        'ffmpeg_location': FFMPEG_PATH,
        'quiet': False,  # Allow detailed logs
        'retries': 10,
        'socket_timeout': 300,
        'postprocessors': [
            {
                'key': 'FFmpegMerger',  # Merge video and audio
            },
            {
                'key': 'FFmpegVideoRemuxer',  # Remux to MP4 format
            },
        ],
    }

    # UI responsives
    def run_download():
        try:
            with YoutubeDL(ydl_opts) as ydl:
                for url_to_download in [url]:
                    if abort_flag.is_set():
                        break
                    while pause_flag.is_set():
                        threading.Event().wait(0.1)
                    ydl.download([url_to_download])
        except Exception as e:
            if not abort_flag.is_set():
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
                print(f"Error details: {str(e)}")  # Log technical details
            progress_var.set(0)

    threading.Thread(target=run_download).start()

# Function to select the storage folder
def select_folder():
    folder = filedialog.askdirectory()
    if folder:
        folder_var.set(folder)

# Create the main window
app = Tk()
app.title("Videonix")
app.geometry("600x400")
app.resizable(False, False)

# background color
app.configure(bg="black")

#Directory for the window icon
app.iconbitmap('C:/Users/Moshin/OneDrive/Desktop/videonix/assets/appicon.ico')

# Get URL Input
Label(app, text="Paste Video URL:", font=("Arial", 12), bg="black", fg="white").place(x=20, y=30)
url_var = StringVar()
Entry(app, textvariable=url_var, font=("Arial", 12), width=35).place(x=200, y=30)

#Folder where to store dowloaded videos
Label(app, text="Select Folder:", font=("Arial", 12), bg="black", fg="white").place(x=20, y=80)
folder_var = StringVar()
Entry(app, textvariable=folder_var, font=("Arial", 12), width=30).place(x=200, y=80)
Button(app, text="Browse", command=select_folder, font=("Arial", 10), bg="white", fg="black").place(x=500, y=75)

# Progress Bar
Label(app, text="Download Progress:", font=("Arial", 12), bg="black", fg="white").place(x=20, y=150)
progress_var = StringVar()
progress_bar = ttk.Progressbar(app, orient="horizontal", length=500, mode="determinate", variable=progress_var)
progress_bar.place(x=50, y=200)

# Download Button
Button(app, text="Download", command=download_video, font=("Arial", 12), bg="white", fg="black", width=15).place(x=250, y=300)

# Stop and Pause Buttons
stop_button = Button(app, text="Stop", command=stop_download, font=("Arial", 12), bg="red", fg="white", width=10)
stop_button.place(x=450, y=300)

pause_button = Button(app, text="Pause", command=toggle_pause, font=("Arial", 12), bg="green", fg="white", width=10)
pause_button.place(x=50, y=300)

# Mohsin's Tool Name
title_label = Label(app, text="Videonix", font=("Arial", 16), bg="black", fg="#ADD8E6")
title_label.place(x=200, y=5)

# Running the application
app.mainloop()
