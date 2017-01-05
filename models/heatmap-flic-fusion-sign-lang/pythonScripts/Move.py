import pysrt
import sys
import os
import shutil

reload(sys)
sys.setdefaultencoding('utf-8')

#Main Function
if __name__ == '__main__':
    subs = pysrt.open(str(sys.argv[1]),encoding='iso-8859-1') #input srt file
    src = str(sys.argv[2]) #input source location
    
    frameRate = 30; #frame rate of the video
    
    #get the youtube link
    fileName = str(sys.argv[1]).split('-')
    fileName = fileName[1].split('.')
    fileName = fileName[0]
    
    for sub in subs:
        
        #get start and end times of subtitles
        startTime = int(sub.start.hours*3600 + sub.start.minutes*60 + sub.start.seconds)
        endTime = int(sub.end.hours*3600 + sub.end.minutes*60 + sub.end.seconds)
        
        #determine start and end frames numbers
        if startTime == 1:
            startFrame = 1
        else:
            startFrame = 30*(startTime)
    
        endFrame = 30*endTime
        #keep a count of # of subtitles
        
        #create a destination folder for the frames resp to this subtitle
        dest = src + fileName + '_' +str(startFrame) + '_' +str(endFrame)+ '/'
        if not os.path.exists(dest):
            os.makedirs(dest)
            
        #save the subtitle
        subtitle_dest_name = str(dest + fileName + '_' +str(startFrame) + '_' +str(endFrame) + ".txt").encode('utf-8')
	with open(subtitle_dest_name , "w") as text_file:
            text_file.write(str(sub.text).encode('utf-8'))
        
        subCount = 0;
        #loop throught the # of frames and move the files to dest folder
        for index in range(startFrame, endFrame):
            subCount = subCount + 1
            oldFile = src + str(index) + '.png'
            newFile = dest + str(subCount) + '.png'
            if os.path.isfile(oldFile):
                shutil.move(oldFile, newFile)

print 'Done.....'
