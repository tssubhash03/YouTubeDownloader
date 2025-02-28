import yt_dlp

video_url = "https://youtu.be/lvO88XxNAzs?si=cNJYvvJQeybNVv7h"  # Your video link
resolution = 2160  # Set desired resolution (e.g., 360, 480, 720, 1080). Leave None for max.
save_folder = "D:/YT_Videos/"  # Change this to your desired folder

# Dynamically set the format based on resolution
if resolution:
    video_format = f"bestvideo[height<={resolution}]+bestaudio/best"
else:
    video_format = "bestvideo+bestaudio/best"  # Maximum resolution

ydl_opts = {
    'format': video_format,  
    'outtmpl': f'{save_folder}%(title)s.%(ext)s',  # Save file with title in the specified folder
    'merge_output_format': 'mp4',  # Ensures proper merging
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

print(f"Download complete! Saved in: {save_folder}")
