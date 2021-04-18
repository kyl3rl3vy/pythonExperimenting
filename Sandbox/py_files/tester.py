import os
import shutil
#def move():

#Get relative path to py file

#Grab all files around py file in same dir and move to folder '01 - Unsorted'

#Make the rest of the folders

#move()



os.system('mkdir "01 - Unsorted"')

currentPath = os.getcwd()
newPath = currentPath+"\\01 - Unsorted"

src = currentPath
dst = newPath

print(src)
print(dst)
list = os.listdir()

for e in list:
    shutil.move(os.path.join(currentPath, e), newPath)
