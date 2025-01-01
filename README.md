
# Videonix Downloader

Videonix Downloader is a powerful and user-friendly video downloader tool designed to simplify the process of downloading and processing videos from various online platforms. Built with Python and integrated with `yt_dlp` and `FFmpeg`, Videonix delivers high-quality video and audio downloads in a standalone executable, eliminating the need for complicated setups.

---

## Features

- **Simple GUI:** Built with Tkinter for ease of use.
- **High-Quality Downloads:** Download videos and audio in the best available quality.
- **Seamless Merging:** Merge video and audio seamlessly using FFmpeg.
- **Download Control:** Pause, resume, and stop downloads as needed.
- **Standalone Executable:** End-users do not need to set up Python or other dependencies.

---

## How to Package Videonix

If you want to package Videonix into a standalone executable, follow these steps:

### Prerequisites
Ensure you have the following installed on your system:

- Python 3.9 or newer (Python 3.13 preferred).
- `pip` (Python's package manager).
- `FFmpeg` (ensure it's accessible in the tool's `ffmpeg/bin` directory).
- **VLC Media Player:** Recommended for optimal compatibility with downloaded videos.

### Install Dependencies

Clone the repository:

```bash
git clone https://github.com/D4rkSynt4x/Videonix-Downloader.git
cd Videonix-Downloader
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

### Package the Tool

Use `PyInstaller` to create a standalone executable:

Install PyInstaller:

```bash
pip install pyinstaller
```

Package the tool:

```bash
pyinstaller --onefile --icon=assets/appicon.ico videonix.py
```

The packaged executable will be located in the `dist/` folder as `videonix.exe`.

---

## How to Use the Packaged Tool

After packaging, you can use the tool as a standalone executable.

### Run the Executable

Double-click the `videonix.exe` file in the `dist/` folder, or run it from the terminal:

```bash
./dist/videonix.exe
```

### Features in the GUI

- **Paste Video URL:** Input the URL of the video you want to download.
- **Select a Folder:** Choose the folder to save the downloaded file.
- **Download:** Click "Download" to start the process. The tool automatically merges video and audio.
- **Pause/Resume:** Pause or resume downloads at any time.
- **Stop:** Stop the download process if needed.

### Important Notes

- The tool may occasionally display an error message at the end of the download. This error has no impact on the downloaded file. We are actively working to resolve this issue in future updates.
- The videos downloaded by this tool are mostly compatible with **VLC Media Player**. Using VLC is highly recommended for the best playback experience.

---

## Advanced Usage

If you need to modify or extend the tool:

1. Edit the `videonix.py` file to add new features or improve functionality.
2. Rebuild the executable using `PyInstaller`.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository and clone it locally.
2. Create a feature branch:

   ```bash
   git checkout -b feature-branch
   ```

3. Commit your changes and push them to GitHub.
4. Open a pull request with a description of your changes.

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it with proper attribution.

---

Thank you for using Videonix Downloader! If you encounter any issues or have suggestions for improvement, feel free to open an issue on GitHub.
