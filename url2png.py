from depot.manager import DepotManager
from selenium import webdriver
import os
import sys
import shutil
import os.path

max_url_save=433

dir_cur=os.path.dirname(os.path.realpath(__file__))+"/"
if len(sys.argv) < 2:
	print "Insufficient param, tell which file to load as url lines."
	sys.exit(0)


file_url=dir_cur+sys.argv[1]+".urls"

param_out=sys.argv[1] or sys.argv[2]
dir_output=dir_cur+param_out+"/"

if not os.path.exists(dir_output):
    os.makedirs(dir_output)

print "Input file:"+file_url
print "Output dir:"+dir_output

if not os.path.isfile(file_url):
	print "Input file not found! Nothing to do here, lets go."
	sys.exit(0)

file_log=dir_cur+sys.argv[1]+'.map'

print "Fetching %s" % file_url
lines = [line.rstrip('\n') for line in open(file_url)]
url_count=len(lines)
print "Total url found:%d, will fetch:%d" %(url_count,min(url_count,max_url_save))
url_count=min(url_count,max_url_save)




phantomjs_path = "C:/Python27/misc/phantomjs-2.1.1-windows/bin/phantomjs.exe"
depot = DepotManager.get()

driver = webdriver.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
driver.set_window_size(1400, 1000) # set the window size that you need 
print "Browser loaded"

ll_file=open(file_log,"w")

count = 0
while (url_count>0 and count < max_url_save):
    
    urn=lines[count]
    
    driver.get(urn)
    file_name=dir_output+"/%d.png" % (count)
    driver.save_screenshot(file_name)
    ll_file.write("%d,%s\n"%(count,urn))
    print "[saved] %d. %s" %(count,urn)
    count+=1

print "Finish!"