import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
import os
import glob
import shutil

# Start of the GUI #
root = tk.Tk()

currentFileName = "fileSorter_v5.py"

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#logo
#logo = Image.open()
#logo = ImageTk.PhotoImage(logo)
#logo_label = tk.Label(image=logo)
#logo_label.image = logo
#logo_label.grid(column=1, row=0)

#instructions
instructions = tk.Label(root, text='Click start to sort the current folder', font='Raleway')
instructions.grid(columnspan=3, column=0, row=1)

#function
def do():
    browse_text.set('loading...')

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

    #Self Destruct

    from os import remove
    from sys import argv

    remove(argv[0])

    browse_text.set('Done!')

    quit()

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, command=lambda:do(), textvariable=browse_text, font='Raleway', bg='#20bebe', fg='white', height=2, width=15)
browse_text.set('Start')
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=100)
canvas.grid(columnspan=3)

# End of the GUI #
root.mainloop()
