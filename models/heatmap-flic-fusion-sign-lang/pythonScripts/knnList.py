import os
from os import listdir
from os.path import isfile, join
import glob
import numpy as np
import sys
sys.path.insert(0,'/hdd2/Ananth/code/skip-thoughts/')
import skipthoughts
reload(sys)
sys.setdefaultencoding('utf-8')

## Load skipthought model
#model = skipthoughts.load_model()

## Image list text output
output = str("/hdd2/datasets/ASL/knnFile.txt")
##trainLabelList = str("/hdd2/Ananth/code/caffe-heatmap/models/heatmap-flic-fusion-sign-lang/trainLabelList.txt")

## The source files
mypath = str("/hdd2/datasets/ASL/frames/")

## Get the root directory
Root = [d for d in os.listdir(mypath) if os.path.isdir(os.path.join(mypath, d))]
Root.sort()
count = 0;

## For each folder in Root, get the list of sub-folders in which images and its annotations are located
for root in Root:
        dirs = [d for d in os.listdir(mypath+'/'+root) if os.path.isdir(os.path.join(mypath+'/'+root, d))]
	dirs.sort()
	if count >= 11: ## Vectors are generated for the first 11 Root folders only
      	 	sys.exit()

        for subdir in dirs:
            
	    #print 'Currently working on: ' + root + ' '  + subdir
	    listOfFiles = glob.glob(mypath + root + '/' + subdir + "/*.png") #list of images
            textFile = glob.glob(mypath + root + '/' + subdir + "/*.txt") #the text file in this sub-folder
	    vectorFile = glob.glob(mypath + root + '/' + subdir + "/*.out") #the out` file in this sub-folder
            #print 'textFile: ',textFile
	    #print 'vectorFile: ',vectorFile
	    with open(output , "a") as text_file:
                    text_file.write(str(vectorFile[0] + ' ' + textFile[0] +'\n').encode('utf-8'))

            #with open(str(textFile[0]),"r") as f:
            #    content = f.readlines()
            
	    #if len(content) > 1: #if the length is more than 1, bring everything in one line
            #    temp = str('');
            #    for c in content:
            #        temp = temp + ' ' + c
            #else:
            #    temp = content[0]
	    
            #print str(temp)
            #inputSentence = [str(temp)] ##encode the sentence as a vector
            #vectors = skipthoughts.encode(model, inputSentence) ## This is the encoded vector of dimension 4800 X 1

            #print vectorName
            #vectorName = mypath + root + '/' + subdir + '/vector.out'
            #np.savetxt(vectorName,vectors[0,2400:4800]) ## We need the last 2400 dimension only as the paper suggests bi-directional is good
	    
            ## For each image, get the name and its corresponding label (vector)
            ## and store in the form: path/to/image/name.png path/to/vector/name.out
            #for image in listOfFiles:
            #    image = str(image)
            #    vectorName = mypath + root + '/' + subdir + '/vector.out'
            #    with open(output , "a") as text_file:
            #        text_file.write(str(image + ' ' + vectorName +'\n').encode('utf-8'))
	count = count + 1;
