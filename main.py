import os
from pytube import YouTube


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

#gettting yt video Options
options = bestQuality(YouTube(link))

for i in range(len(options)):
    print(str(i+1) + ". " + str(options[i].resolution))

#requesting video choice
streamDownload = int(input("Which video quality would you like to download?"))

#getting directory
path = os.getcwd()
savingPath = str(path) + "\downloads"

print("Downloading Option " + str(streamDownload) + ". " + str(options[streamDownload-1].resolution))
print("Saving in Path: " + savingPath)

options[streamDownload-1].download(savingPath)
print("Finished Downloading")