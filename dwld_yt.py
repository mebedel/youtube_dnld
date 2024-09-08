import os
import platform
import yt_dlp

def download_videos(channel_url, quality):
    # Get the current platform (Windows, Linux, etc.)
    system_platform = platform.system()

    # Define the ffmpeg executable name depending on the platform
    if system_platform == "Windows":
        ffmpeg_exec = 'ffmpeg.exe'
    else:
        ffmpeg_exec = 'ffmpeg'
    
    # Create the full path to ffmpeg
    ffmpeg_path = os.path.join(os.path.dirname(__file__), ffmpeg_exec)
    
    if quality == 'best':
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s',
            'ffmpeg_location': ffmpeg_path,
        }
    elif quality == 'worst':
        ydl_opts = {
            'format': 'worst',
            'outtmpl': '%(title)s.%(ext)s',
            'ffmpeg_location': ffmpeg_path,
        }
    else:
        # If the user provides a specific resolution (e.g., "720p")
        ydl_opts = {
            'format': f'bestvideo[height<={quality}]+bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'ffmpeg_location': ffmpeg_path,
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([channel_url])

if __name__ == "__main__":
    channel_url = input("Enter the YouTube channel URL: ")
    print("Select video quality: ")
    print("1. Best quality")
    print("2. Worst quality")
    print("3. Enter specific resolution (e.g., 720 for 720p)")
    
    choice = input("Enter your choice (1, 2, or resolution): ")
    
    if choice == '1':
        quality = 'best'
    elif choice == '2':
        quality = 'worst'
    else:
        quality = choice  # Assume the user entered a specific resolution
    
    download_videos(channel_url, quality)
