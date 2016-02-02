import os
from mutagen.easyid3 import EasyID3, mutagen
from mutagen.easymp4 import EasyMP4
extensions = [".mp3"]
tags_names = ["TPE1", "TCON", "TALB", "TIT2", "TPUB", "TRCK"]
listdir = []
for x in os.listdir(path="."):
    file = os.path.splitext(x)
    if(file[1] in extensions) :
        listdir.append(file)
print("LIST OF FILES:\t", listdir)

for file in listdir:
    name = file[0]+file[1]
    m = mutagen.File(name)
    tag = dict.fromkeys(tags_names)
    for t in tag.keys():
        tag[t] = m[t]
        print(t, tag[t])
    os.rename(name, "{0} - {1}{2}".format(tag["TRCK"], tag["TIT2"], file[1]))
    print("_______")
