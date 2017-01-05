import sys
import glob
import os

reload(sys)
sys.setdefaultencoding('utf-8')

#Main Function
if __name__ == '__main__':
    mypath = str(sys.argv[1])
    destPath = str(sys.argv[2])
    listOfFiles = glob.glob(mypath + "*.vtt")
    temp = " \n".join(str(s) for s in listOfFiles)

    with open(destPath+"listOfVideos.txt", "w") as text_file:
        text_file.write(str(temp).encode('utf-8'))