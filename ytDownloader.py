from pytube import YouTube
from sys import argv
from pathlib import Path

link = argv[1]

#change link for new videos!
yt = YouTube('https://www.youtube.com/watch?v=iogcY_4xGjo') 

print("Title :", yt.title)
print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()
yd.download('Path for downloaded videos')

#terminal: python ytDownloader.py "https://www.youtube.com/watch?v=iogcY_4xGjo"
