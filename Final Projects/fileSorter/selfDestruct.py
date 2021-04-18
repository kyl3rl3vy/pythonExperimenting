import os
import shutil

currentDir = os.getcwd()
print(currentDir)

os.chdir('../')
print(os.getcwd())

#shutil.move(__file__, os.getcwd())

from os import remove
from sys import argv

remove(argv[0])
