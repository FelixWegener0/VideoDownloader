from pytube import YouTube
from moviepy.editor import *
import os

def downloadToPath(url):
    path = './videos'
    video = YouTube(url)
    video = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    video.download(path)
    print('downloaded')

def mp4ToMp3():
    print('changing format to mp3')
    mp4 = os.listdir('./videos')
    mp3 = mp4[0].replace('mp4','mp3')
    FILETOCONVERT = AudioFileClip('./videos/' + mp4[0])
    FILETOCONVERT.write_audiofile('./videos/' + mp3)
    FILETOCONVERT.close()
    os.remove('./videos/' + mp4[0])

if (__name__ == '__main__'):
    url = input('insert the youtube video Url:')
    downloadToPath(url)
    mp4ToMp3()
    