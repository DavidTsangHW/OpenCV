# importing the module 
from pytube import YouTube 
  
# where to save 
SAVE_PATH = "X:\\OpenCV" #to_do 

link="https://www.youtube.com/watch?v=utZrDfArOqE&t=10s"

print("Downloading")

yt = YouTube(link)
stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download()

stream.download(SAVE_PATH)

print('Task Completed!')

