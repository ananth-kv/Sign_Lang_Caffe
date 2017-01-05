import sys
import glob
import os

if __name__ == '__main__':

    #print "usage: ImageCrop.py /folder/path 345 435 34 56 (W H X Y)"
    mypath = str(sys.argv[1])
    width = str(sys.argv[2])
    heigth = str(sys.argv[3])
    x = str(sys.argv[4])
    y = str(sys.argv[5])
    count = 0;
    for subdir in os.listdir(mypath):

        listOfFiles = glob.glob(mypath+subdir+"/*.png")

        for itemFile in listOfFiles:
            ffmpeg = "ffmpeg -i {0} -y -vf \"crop = {1}:{2}:{3}:{4}\" {5}".format(itemFile,width,heigth,x,y,itemFile)
            os.system(ffmpeg)
	    count = count + 1

print "Total # of images cropped: "+ str(count)
print "Everything's Done..."
