from pytube import YouTube
from pytube import Playlist
import os
from moviepy.audio.io.AudioFileClip import AudioFileClip
import re


class YoutubeConverter:
    
    def __init__(self, link, pasta):

        try:
            yt = YouTube(link) 

            yt.streams.filter(only_audio=True).first().download(pasta)


        except:
            yt = Playlist(link)

            yt.video_urls
            for url in yt:
                YouTube(url).streams.filter(only_audio=True).first().download(pasta)



        
        for file in os.listdir(pasta):
            if re.search('mp4', file):
                mp4_path = os.path.join(pasta,file)
                mp3_path = os.path.join(pasta,os.path.splitext(file)[0]+'.mp3')
                new_file = AudioFileClip(mp4_path)
                new_file.write_audiofile(mp3_path)
                os.remove(mp4_path)
