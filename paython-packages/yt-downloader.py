from pytube import YouTube

link = input("Enter the link: ")
yt = YouTube(link)
videos = yt.streams.all()

video = list(enumerate(videos))

for i in videos:
    print(i)
    
print("Enter the number of the video you want to download: ")

option = int(input(" enter the number: "))

dwn_video = videos[option]

dwn_video.download()

print("Download complete")