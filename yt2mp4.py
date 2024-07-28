import os
import yt_dlp

def download_video(url, download_directory):
    # Check if the directory exists, if not, create it
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',  # Ensure the best video and audio in MP4 format
        'outtmpl': os.path.join(download_directory, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',  # Merge format set to MP4
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    # Example usage
    video_url = 'https://youtu.be/XFkzRNyygfk'  # Replace with your video URL
    download_path = 'D:/School Programs'  # Replace with your desired download directory

    download_video(video_url, download_path)
