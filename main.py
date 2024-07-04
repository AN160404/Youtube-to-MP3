from pytube import YouTube
from moviepy.editor import *
url=input("Enter url:\n")
yt=YouTube(url)
print("What do you want to download?\n")
print("1. Download Video")
print("2. Download Audio")
option=int(input("Enter option:\n"))
if(option==1):
    stream=yt.streams.get_highest_resolution()
    stream.download()
    print("Downloaded!")
elif(option==2):
    stream=yt.streams.get_audio_only()
    stream.download()
    print("Downloaded!!")
else:
    print("Enter valid option")
