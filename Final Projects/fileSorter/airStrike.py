#PDF text extractor

import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askdirectory
import shutil
import os

# Start of the GUI #
root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

#instructions
instructions = tk.Label(root, text='Select destination folder')
instructions.grid(columnspan=3, column=0, row=1)


#definitions
src = os.path.join(os.getcwd(),'bomb.py')

#function
def open_folder():
    browse_text.set('loading...')
    folder = askdirectory(parent=root, title='Select a file')
    if folder:

        print(folder)
        dst = folder
        shutil.copy(src,dst)

        browse_text.set('Got it!')

        os.chdir(folder)

        os.system('python ' + dst+'\\bomb.py')

#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, command=lambda:open_folder(), textvariable=browse_text, font='Raleway', bg='#20bebe', fg='white', height=2, width=15)
browse_text.set('Browse')
browse_btn.grid(column=1, row=2)

canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

# End of the GUI #
root.mainloop()
