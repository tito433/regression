from depot.manager import DepotManager
from selenium import webdriver
import sys
import shutil
import glob, os

max_url_save=400

dir_cur=os.path.dirname(os.path.realpath(__file__))+"/"
if len(sys.argv) < 2:
	print "Insufficient param, tell which file to load as url lines."
	sys.exit(0)


dir_output=dir_cur+sys.argv[1]+"/"
if not os.path.exists(dir_output):
    print dir_output+" does not exist. I will exit now."
    sys.exit(0)

os.chdir(dir_output)
for file in glob.glob("*.urls"):
    file_url=file

if not os.path.isfile(file_url):
	print "Input file [%s] not found! Nothing to do here, lets go." % (file_url)
	sys.exit(0)

print "Input file:"+file_url

file_log=sys.argv[1]+'.map'
print "Output log:"+file_log
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

ll_file=open(file_log,"w",0)
llen=len(lines)
count = 0
while (count<llen and count<url_count):
    
    urn=lines[count]
    
    driver.get(urn)
    file_name=count+".png"
    driver.save_screenshot(file_name)
    ll_file.write("%d,%s\n"%(count,urn))
    print "[saved] %d. %s" %(count,urn)
    count+=1

print "Finish!"