# importing the module 
from pytube import YouTube 
  
# where to save 
SAVE_PATH = "X:\\OpenCV" #to_do 

link="https://www.youtube.com/watch?v=3slCiigH2BU"

print('Enter YouTube link:')

link = input()

print("Downloading")

yt = YouTube(link)

youtube = YouTube(link)

i = 0

for a in youtube.streams:
    print(a)

i = -1

print('Enter itag to download')

i = int(input())

stream = youtube.streams.get_by_itag(i)

stream.download()


#stream = youtube.streams.filter(progressive=False, file_extension='mp4', type='video').order_by('resolution')[-1].download()

#youtube.streams.first().download()


exit()

stream = youtube.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()

#stream.download(SAVE_PATH)

print('Task Completed!')

