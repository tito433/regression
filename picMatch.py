import cv2
import numpy as np
import os
import sys
from os import listdir
from os.path import isfile, join
import shutil


dir_src=sys.argv[1]
dir_dist=sys.argv[2]
dir1_pic=os.path.dirname(os.path.realpath(__file__))+"/"+dir_src+"/"
dir2_pic=os.path.dirname(os.path.realpath(__file__))+"/"+dir_dist+"/"
dir_output=os.path.dirname(os.path.realpath(__file__))+"/miss/"

if os.path.isdir(dir_output):
	shutil.rmtree(dir_output, ignore_errors=True)

if not os.path.exists(dir_output):
    os.makedirs(dir_output)
    
print "dir1:%s, dir2:%s" %(dir1_pic,dir2_pic)

def resizeImge(w,h,img):
	h1, w1=img.shape
	vis = np.zeros((max(h, h1), max(w,w1)), np.float32)
	m = cv2.cvtColor(vis, cv2.COLOR_GRAY2BGR)

	vis[:h1, :w1] = img
	
	return vis

for f in listdir(dir1_pic):
	print "Matching:%s" %(f)
	if isfile(join(dir1_pic, f)) and isfile(join(dir2_pic, f)):
		image1 = cv2.imread(dir1_pic+f,0)
		h1, w1=image1.shape
		image2 = cv2.imread(dir2_pic+f,0)
		h2, w2 = image2.shape

		h=max(h1,h2)
		w=max(w1,w2)

		image1=resizeImge(w,h,image1)
		image2=resizeImge(w,h,image2)

		diff = cv2.absdiff(image1, image2)
		cv2.imwrite(dir_output+f,diff)




#cv2.drawContours(img1, contours, -1, (0,255,0), 3)
#cv2.imwrite(dir_output+'0.png',img1)


print "Done!"
