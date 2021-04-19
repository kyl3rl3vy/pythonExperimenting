#Simple Python Script To arrange your files in one click
from tkinter import *
import os
import glob
import shutil

root = Tk()

currentFileName = "fileSorter_v4.py"

def myClick():
    #glob function of glob module to detect all files inside current directory
    files_list = glob.glob("*")
    #Creating a set of extension types inside the folder to avoid duplicate entries
    extension_set = set()
    #adding each type of extension to the set
    for file in files_list:
        extension = file.split(sep=".")
        try:
            extension_set.add(extension[1])
        except IndexError:
            continue

    extension_set2 = []

    for item in extension_set:
        if item != "py":
            extension_set2.append(item)

    extension_set = extension_set2

    print(extension_set)
    #Function to create directory for each type of extension
    def createDirs():
        for dir in extension_set:
            try:
                os.makedirs(dir.upper())
            except FileExistsError:
                continue

    #Function to move files to respective folders
    def arrange():
        for file in files_list:
            fextension = file.split(sep=".")
            try:
                os.rename(file, fextension[1].upper()+"/"+file)
            except (OSError, IndexError):
                continue

    #Move new folders into sorted files_list



    def move():

        os.system('mkdir "01 - Unsorted"')

        currentPath = os.getcwd()
        newPath = currentPath+"\\01 - Unsorted"

        src = currentPath
        dst = newPath

        print(src)
        print(dst)
        list = os.listdir()

        list2 = []

        for item in list:
            if item != currentFileName:
                list2.append(item)

        list = list2

        print(list)

        for e in list:
            shutil.move(os.path.join(currentPath, e), newPath)



    #Calling the functions in order
    createDirs()
    arrange()
    move()

    #Make other organizational folders
    os.system('mkdir "02 - Sorted" "03 - Edited" "04 - Exported"')

myButton = Button(root, text='Press to start', padx = 100, pady = 100, command=myClick)
myButton.pack()

root.mainloop()


#Self Destruct

from os import remove
from sys import argv

remove(argv[0])
