from pytube import YouTube
from moviepy.editor import AudioFileClip
import os
import sys


def downloadToPath(url):
    path = './videos'
    video = YouTube(url)
    video = video.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    video.download(path)
    print('downloaded')


def mp4ToMp3():
    print('changing format to mp3')
    mp4 = os.listdir('./videos')
    mp3 = mp4[0].replace('mp4', 'mp3')
    convertFile = AudioFileClip('./videos/' + mp4[0])
    convertFile.write_audiofile('./videos/' + mp3)
    convertFile.close()
    os.remove('./videos/' + mp4[0])


if (__name__ == '__main__'):
    if (not sys.argv[1]):
        url = input('insert the youtube video Url:')
    else:
        url = sys.argv[1]
    downloadToPath(url)
    mp4ToMp3()
