from pytube import YouTube
import os

def downloadToPath(url):
    path = './videos'
    video = YouTube(url)
    video = video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists(path):
        os.makedirs(path)
    video.download(path)

if (__name__ == '__main__'):
    url = input('insert the youtube video Url:')
    downloadToPath(url)
    print('downloaded')