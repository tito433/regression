import cv2
import numpy as np
import os
import sys
from os import listdir
from os.path import isfile, join

dir_src=sys.argv[1]
dir_dist=sys.argv[2]
dir1_pic=os.path.dirname(os.path.realpath(__file__))+"/"+dir_src+"/"
dir2_pic=os.path.dirname(os.path.realpath(__file__))+"/"+dir_dist+"/"
dir_output=os.path.dirname(os.path.realpath(__file__))+"/miss/"

print "dir1:%s, dir2:%s" %(dir1_pic,dir2_pic)


for f in listdir(dir1_pic):
	print "Matching:%s" %(f)
	if isfile(join(dir1_pic, f)) and isfile(join(dir2_pic, f)):
		img1a = cv2.imread(dir1_pic+f)
		img1 = cv2.cvtColor( img1a, cv2.COLOR_RGB2GRAY)
		ret,thresh = cv2.threshold(img1,0, 255, cv2.THRESH_OTSU)
		cont1,hier2 = cv2.findContours(thresh, 1, 2)

		img2a = cv2.imread(dir2_pic+f)
		img2 = cv2.cvtColor(img2a,cv2.COLOR_RGB2GRAY)
		ret,thresh = cv2.threshold(img2,0, 255, cv2.THRESH_OTSU)
		cont2,hier2 = cv2.findContours(thresh, 1, 2)

		if len(cont1) != len(cont2):
		    print "Missmatch: %s" % f
		    diff = cv2.absdiff(img1a, img2a)
		    #cv2.drawContours(img1, diff, -1, (0,255,0), 3)
		    cv2.imwrite(dir_output+f,diff)



#cv2.drawContours(img1, contours, -1, (0,255,0), 3)
#cv2.imwrite(dir_output+'0.png',img1)


print "Done!"
