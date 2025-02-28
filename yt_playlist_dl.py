import yt_dlp

# YouTube playlist URL (Replace with the actual playlist link)
playlist_url = "https://youtube.com/playlist?list=PLMCXHnjXnTnvo6alSjVkgxV-VH6EPyvoX&si=jh_8ulrimInptZ8Q"

# Set desired resolution (e.g., 360, 480, 720, 1080). Use None for max resolution.
resolution = 720  

# Set custom folder path to save videos
save_folder = "D:/YT_Playlist_Videos/"

# Dynamically set the format based on resolution
if resolution:
    video_format = f"bestvideo[height<={resolution}]+bestaudio/best"
else:
    video_format = "bestvideo+bestaudio/best"

ydl_opts = {
    'format': video_format,  
    'outtmpl': f'{save_folder}%(playlist)s/%(playlist_index)s - %(title)s.%(ext)s',  
    'merge_output_format': 'mp4',  
    'noplaylist': False,  # Ensures full playlist download
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([playlist_url])

print(f"Playlist download complete! Saved in: {save_folder}")
