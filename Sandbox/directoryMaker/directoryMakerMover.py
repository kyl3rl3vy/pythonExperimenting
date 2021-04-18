import os, shutil

os.chdir('C:\\Users\Kyle\Programming Projects\Sandbox\directoryMaker')
os.system('mkdir "01 - Unsorted" "02 - Sorted" "03 - Edited" "04 - Exported"')
os.system('mkdir "pythonFile"')
shutil.move('C:\\Users\Kyle\Programming Projects\Sandbox\directoryMaker\directoryMakerMover.py',
            'C:\\Users\Kyle\Programming Projects\Sandbox\directoryMaker\pythonFile')

#os.chdir('directory to move into')
#os.system('cmd or terminal command')
#shutil.move('source', 'final destination')
