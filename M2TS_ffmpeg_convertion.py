#Import the necessary addons
import os

#Ask for folder directory
print("Input the m2ts folder directory")
from tkinter.filedialog import askdirectory
path = askdirectory(title='Select Folder') # shows dialog box and return the path
print(path)

#Ask for file count
print("Input the number of m2ts files to convert")
num = input ("Enter number :")
print(num)

#Prepare the primary number and current number variable
prinum = int(num)
curnum = prinum

#Initiate loop prinum times
for i in range(prinum):
    
    #Open CMD and input command
    os.chdir('{}'.format(path))
    os.system('start /wait cmd /c ffmpeg -i input' + str(curnum) + '.m2ts -vcodec libx264 -crf 20 -acodec ac3 -vf "yadif" output' + str(curnum) + '.mp4')

    #Delete one instance of converted files
    curnum -= 1

#Return finish message and stop program
print("Convertion finished")
exit()
