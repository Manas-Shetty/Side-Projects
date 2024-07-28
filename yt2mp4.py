import os
import yt_dlp
import subprocess

def download_video(url, download_directory):
    # Check if the directory exists, if not, create it
    if not os.path.exists(download_directory):
        os.makedirs(download_directory)

    temp_file = os.path.join(download_directory, 'temp.%(ext)s')
    output_file = os.path.join(download_directory, '%(title)s.mp4')

    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',
        'outtmpl': temp_file,
        'merge_output_format': 'mp4',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    # Re-encode the video using ffmpeg for compression
    temp_mp4 = temp_file.replace('%(ext)s', 'mp4')
    final_mp4 = output_file.replace('%(ext)s', 'mp4')
    ffmpeg_command = [
        'ffmpeg', '-i', temp_mp4, '-vcodec', 'libx264', '-crf', '28', '-preset', 'slow', final_mp4
    ]
    subprocess.run(ffmpeg_command)

    # Remove the temporary file
    os.remove(temp_mp4)

if __name__ == "__main__":
    # Example usage
    video_url=input("Enter the URL of the video: ")
    download_path = 'D:/School Programs'  # Replace with your desired download directory

    download_video(video_url, download_path)
