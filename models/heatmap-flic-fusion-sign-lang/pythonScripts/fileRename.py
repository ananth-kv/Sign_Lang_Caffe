import os
import sys
import glob
import shutil

if __name__ == '__main__':

    mypath = str(sys.argv[1])
    
    for itemFile in os.listdir(mypath):
        
        newFile = itemFile.replace(' ','').replace(',','').replace('!','').replace('(','').replace(')','').replace('!','').replace('&','')
        os.rename(itemFile, newFile)
        
    print 'done'