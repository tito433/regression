import cv2
import numpy as np
import sys
import shutil
import glob, os
import re

def getImageByUrl(lines,url):
	for line in lines:
		idx,ur=[x for x in map_pattern.split(line) if x]
		if ur == url:
			return idx

	return -1

def resizeImge(w,h,img):
	h1, w1=img.shape
	vis = np.zeros((max(h, h1), max(w,w1)), np.float32)
	m = cv2.cvtColor(vis, cv2.COLOR_GRAY2BGR)

	vis[:h1, :w1] = img
	
	return vis



dir_cur=os.path.dirname(os.path.realpath(__file__))+"/"
if len(sys.argv) < 2:
	print "Insufficient param, tell me which folder has the map files?"
	sys.exit(0)

dir_test=os.path.join(dir_cur,sys.argv[1])


if not os.path.isdir(dir_test):
	print "%s is not a valid path! I will exit." %(dir_test)
	sys.exit(0)


files_map=[]
os.chdir(dir_test)
for m in glob.glob("*.map"):
	files_map.append(m[:-4])

dir_output=os.path.join(dir_test,"miss");

if os.path.isdir(dir_output):
	shutil.rmtree(dir_output, ignore_errors=True)

if not os.path.exists(dir_output):
    os.makedirs(dir_output)

if len(files_map)<2:
	print "Not enought mappings! I will exit."
	sys.exit(0)

map_pattern = re.compile("^(\d+),(.*)$")
for i in range(len(files_map)-1):
	map1=files_map[i]
	map2=files_map[i+1]
	print "Mapings: %s and %s" %(map1,map2)
	lines1 = [line.rstrip('\n') for line in open(os.path.join(dir_test,map1+'.map'))]
	lines2 = [line.rstrip('\n') for line in open(os.path.join(dir_test,map2+'.map'))]
	
	for line in lines1:
		id1,url=[x for x in map_pattern.split(line) if x]
		f1=os.path.join(dir_test,map1,id1+".png")

		id2=getImageByUrl(lines2,url)
		if id2>-1:
			f2=os.path.join(dir_test,map2,id2+".png")

		if os.path.isfile(f1) and os.path.isfile(f2):
			f3=os.path.join(dir_test,"miss","%s_+_%s_+_%s_%s.png"%(map1,map2,id1,id2))
			image1 = cv2.imread(f1,0)
			h1, w1=image1.shape
			image2 = cv2.imread(f2,0)
			h2, w2 = image2.shape

			h=max(h1,h2)
			w=max(w1,w2)

			image1=resizeImge(w,h,image1)
			image2=resizeImge(w,h,image2)

			diff = cv2.absdiff(image1, image2)
			cv2.imwrite(f3,diff)



print "Finish!"
