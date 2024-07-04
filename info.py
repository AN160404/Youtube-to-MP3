from pytube import YouTube
from moviepy.editor import *
yt=YouTube('https://youtu.be/EZD-Jy5iiYU?si=ydJrBm4A_SU_HRGK')
print("Title: ",yt.title)
print("Thumbnail: ",yt.thumbnail_url)

# # yt=YouTube('https://youtu.be/EZD-Jy5iiYU?si=ydJrBm4A_SU_HRGK',
# #            on_progress_callback=progress_func,
# #            on_complete_callback=cmplete_func,
# #            proxies=my_proxies,
# #            use_oauth=False,
# #            allow_ouath_cache=True
# #         )
# print(yt.streams) #DASH streams: audio and video in different files.
# print(yt.streams.filter(progressive=True)) #Progressive streams: they have audio and video in a single file but don't provide highest quality
# print(yt.streams.filter(only_audio=False)) #only conatins the audio track
# print(yt.streams.filter(file_extension='mp4')) #only conatins the mp4 track
# a=input("Enter itag: ")
# stream=yt.streams.get_by_itag(a)

# stream.download()
# # caption=yt.captions.get_by_language_code('ur')
# # print(caption)
streams=yt.streams.get_audio_only()
streams.download()