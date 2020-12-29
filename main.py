import os
from pytube import YouTube
from moviepy.editor import *


def bestQuality(yt):
    ys = yt.streams
    possible_streams = []

    # 4k
    if ys.get_by_itag(313) is not None:
        possible_streams.append(ys.get_by_itag(313))

    if ys.get_by_itag(315) is not None:
        possible_streams.append(ys.get_by_itag(315))

    # 2k
    if ys.get_by_itag(271) is not None:
        possible_streams.append(ys.get_by_itag(271))

    if ys.get_by_itag(308) is not None:
        possible_streams.append(ys.get_by_itag(308))

    # 1080p
    if ys.get_by_itag(137) is not None:
        possible_streams.append(ys.get_by_itag(137))

    if ys.get_by_itag(299) is not None:
        possible_streams.append(ys.get_by_itag(299))

    # 720
    if ys.get_by_itag(136) is not None:
        possible_streams.append(ys.get_by_itag(136))

    # 480p
    if ys.get_by_itag(135) is not None:
        possible_streams.append(ys.get_by_itag(135))
    # 360p
    if ys.get_by_itag(134) is not None:
        possible_streams.append(ys.get_by_itag(134))

    return possible_streams


link = str(input("What is the URL?"))

# gettting yt video Options
options = bestQuality(YouTube(link))

for i in range(len(options)):
    print(str(i + 1) + ". " + str(options[i].resolution))

# requesting video choice
streamDownload = int(input("Which video quality would you like to download?"))

# getting directory
path = os.getcwd()
savingPathVideo = str(path) + "\Video"
savingPathAudio = str(path) + "\Audio"

print("Downloading Option " + str(streamDownload) + ". " + str(options[streamDownload - 1].resolution))
print("Saving Video in Path: " + savingPathVideo)

options[streamDownload - 1].download(savingPathVideo)
print("Finished Downloading Video")

# Not in The Video Just adding Audio To Video
# ----------------------
# Downloading Audio
# --------------------
# Combining Audio With Video
def combine_audio(videoDirectory, audioDirectory, outputDirectory, fps=30):
    # mp4 to mp3
    clip = AudioFileClip(audioDirectory)
    clip.write_audiofile('./Audio/file.mp3')
    clip.close()

    # Mixing
    my_clip = VideoFileClip(videoDirectory)
    audio_background = AudioFileClip('./Audio/file.mp3')
    final_clip = my_clip.set_audio(audio_background)
    final_clip.write_videofile(outputDirectory, fps=fps)

    final_clip.close()

# Save path and download of audio
print("Saving Audio in Path: " + savingPathAudio)
YouTube(link).streams.get_by_itag(140).download(savingPathAudio)
print("Finished Downloading Audio")

# File Locations
base = YouTube(link).title
final = str(base) + ".mp4"

# Audio Combination
combine_audio("./Video/" + final, "./Audio/" + final, "./downloads/final.mp4", fps=60)
print("Done")
