import os
import glob

files_list = glob.glob("*")

extension_set = set()

for file in files:
    extension = file.split(sep=".")
    try:
        extension_set.add(extension[1])
    except IndexError:
        continue

print(extension_set)

def createDirs():
    for dir in extensino_set:
        try:
            os.makefirs(dir+"_files")
        except FileExistError:
            continue

