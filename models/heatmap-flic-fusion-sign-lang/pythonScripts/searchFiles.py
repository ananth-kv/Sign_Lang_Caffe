from os import listdir
from os.path import isfile, join
import sys
import glob
import subprocess
import os

if __name__ == '__main__':
    
    mypath = str(sys.argv[1])
    extension = str(sys.argv[2])
    
    listOfFiles = glob.glob(mypath + "*."+ extension)
    
    for itemFile in listOfFiles:
        
        temp = itemFile.split('.')
        
        videoName =   temp[0] + '.mp4'
        folderName =   temp[0]
        
        if not os.path.exists(folderName):
            os.makedirs(folderName)

        os.system("ffmpeg -i " + videoName + " -r 30 -vf scale=-1:256 -vcodec png " + folderName + "/%d.png")
        
        print "Video Done..."
        
        #print "python Move.py " + itemFile.replace(' ','\ ').replace(',','\,') + " " + folderName + "/"
        os.system("python Move.py " + itemFile + " " + folderName + "/");
        
        print "Files Moved..."

print "------------------------------Everything Done------------------------------"
