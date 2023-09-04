import tkinter as tk
from tkinter import filedialog
import yt_dlp

app_name = "ydl-gui"
app_developer = "Lucas Gabriel (lucmsilva)"
app_short_developer = "lucmsilva"
app_identifier = "[" + app_name + "] "
app_version = "v0.0.0"
app_description = app_identifier + "A modular script to download videos from multiple sites via GUI. Forked from ydl-cli"
app_github_repo = "lucmsilva651/ydl-gui"
app_str_github_link = "https://github.com/"
app_str_dot = " - "
app_str_warningdialog_title = "Warning!"
app_str_warningdialog_content = "If the application becomes unresponsive during the download process, simply wait for the download to complete or check the terminal for progress."
app_str_videourl_request = "Insert the video URL:"
app_str_seloutput = "Selected folder:"
app_str_seloutput_btn = "Choose destination folder"
app_str_downloadvideo_btn = "Download video"
app_str_downloadcompletedialog_title = "Download complete"
app_str_downloadcompletedialog_content1 = "The video "
app_str_downloadcompletedialog_content2 = " has been downloaded with success!"
app_window_title = app_name + app_str_dot + app_short_developer + app_str_dot + app_version
app_window_width = 400
app_window_height = 200
app_outputdir = "videos"

class YouTubeDownloaderApp:
    def __init__(self, root):
        center_window(root, app_window_width, app_window_height)
        print(app_identifier + app_window_title + "\n" + app_identifier + app_str_github_link + app_github_repo + "\n\n" + app_description + "\n")

        self.root = root
        self.root.title(app_window_title)
        tk.messagebox.showwarning(app_str_warningdialog_title, app_str_warningdialog_content)
        self.label = tk.Label(root, text=app_str_videourl_request)
        self.label.pack(pady=10)

        self.url_entry = tk.Entry(root, width=40)
        self.url_entry.pack(pady=5)

        self.browse_button = tk.Button(root, text=app_str_seloutput_btn, command=self.choose_directory)
        self.browse_button.pack(pady=10)

        self.download_button = tk.Button(root, text=app_str_downloadvideo_btn, command=self.download_video)
        self.download_button.pack()

        self.output_directory = app_outputdir

    def choose_directory(self):
        self.output_directory = filedialog.askdirectory()
        if self.output_directory:
            self.browse_button.config(text=app_str_seloutput + self.output_directory)

    def download_video(self):
        url = self.url_entry.get()
        if not url:
            return

        ydl_opts = {
            'format': 'best',
            'outtmpl': f"{self.output_directory}/%(title)s.%(ext)s",
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=False)
            video_title = info_dict.get('title', 'video')

            ydl.download([url])

            tk.messagebox.showinfo(app_str_downloadcompletedialog_title, app_str_downloadcompletedialog_content1 + video_title + app_str_downloadcompletedialog_content2)

def center_window(window, width, height):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        window.geometry(f"{width}x{height}+{x}+{y}")


if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloaderApp(root)
    root.mainloop()
