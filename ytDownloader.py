from pytube import YouTube
from sys import argv
from pathlib import Path


link = argv[1]
#yt = YouTube(link)

#wichtig link ändern, bei neuem Video!!
yt = YouTube('https://www.youtube.com/watch?v=iogcY_4xGjo') 

print("Title :", yt.title)

print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()
yd.download('C:\\Users\\Lambo\\OneDrive - Bildungszentrum Zürichsee\\Dokumente\\Privat\\Projekte\\ytDownloads')

#yd = yt.streams.first()
#yd.download('C:\\Users\\Lambo\\OneDrive - Bildungszentrum Zürichsee\\Dokumente\\Privat\\Projekte\\ytDownloads')

#in Terminal: python ytDownloader.py "https://www.youtube.com/watch?v=vEQ8CXFWLZU&t=68"
#python ytDownloader.py "https://www.youtube.com/@InternetMadeCoder"
#python ytDownloader.py "https://youtu.be/lp0Sxn42TGs"
#python ytDownloader.py "https://www.youtube.com/watch?v=iogcY_4xGjo"
