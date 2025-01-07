import yt_dlp

url = input("Enter a YouTube link to download: ")
ydl_opts = {'format': 'best'}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

#make sure the link is not a list link because it will download all the videos on the list eg
#(https://www.youtube.com/watch?v=7X2TAY0U0LI&list=RD7X2TAY0U0LI&start_radio=1)
"""
By default, yt-dlp downloads all videos in a playlist or any associated
videos unless explicitly instructed to download just the single video.
or add
ydl_opts = {
    'format': 'best',
    'noplaylist': True,  # Ensure only a single video is downloaded
}
"""