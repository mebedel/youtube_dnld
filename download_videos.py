import yt_dlp

def download_videos(channel_url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([channel_url])

if __name__ == "__main__":
    channel_url = input("Enter the YouTube channel URL: ")
    download_videos(channel_url)
