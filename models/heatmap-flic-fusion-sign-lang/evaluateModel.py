import caffe
import numpy as np
import matplotlib.pyplot as plt

## Initiate the net
net = caffe.Net('/hdd2/Ananth/code/caffe-heatmap/models/heatmap-flic-fusion-sign-lang/train_val_new.prototxt', '/hdd2/Ananth/code/caffe-heatmap/snapshots/heatmap-flic-fusion-sign-lang/_iter_1924000.caffemodel', caffe.TEST)

# load input and configure preprocessing
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,0,1))
transformer.set_channel_swap('data', (2,1,0))
#transformer.set_raw_scale('data', 255.0)

## Reshape the images into 256X256
#net.blobs['data'].reshape(1,3,256,256)


#load the image in the data layer
im = caffe.io.load_image('/hdd2/Ananth/code/caffe-heatmap/models/heatmap-flic-fusion-sign-lang/testImages/30.png')

net.blobs['data'].data[...] = transformer.preprocess('data', im)

#compute
out = net.forward(blobs=['fc1'])

print out.keys()

np.savetxt('testImage1.out',out['fc1'])
