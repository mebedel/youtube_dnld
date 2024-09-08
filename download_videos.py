import yt_dlp

def download_videos(channel_url, quality):
    # Define options based on user input for quality
    if quality == 'best':
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s',
        }
    elif quality == 'worst':
        ydl_opts = {
            'format': 'worst',
            'outtmpl': '%(title)s.%(ext)s',
        }
    else:
        # If the user provides a specific resolution (e.g., "720p")
        ydl_opts = {
            'format': f'bestvideo[height<={quality}]+bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
        }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([channel_url])

if __name__ == "__main__":
    channel_url = input("Enter the YouTube channel URL: ")
    print("Select video quality: ")
    print("1. Best quality")
    print("2. Worst quality")
    print("3. Enter specific resolution (e.g., 144 for 144p)")
    
    choice = input("Enter your choice (1 = best quality, 2 = worst quality, or your choice for example 144): ")
    
    if choice == '1':
        quality = 'best'
    elif choice == '2':
        quality = 'worst'
    else:
        quality = choice  # Assume the user entered a specific resolution
    
    download_videos(channel_url, quality)
