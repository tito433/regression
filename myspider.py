import requests
import re
import os
import sys
import shutil
import os.path
from urlparse import urlparse

dir_cur=os.path.dirname(os.path.realpath(__file__))+"/"

#print urlparse(sys.argv[1])
#sys.exit(0)
depth=3
urls=[]

if len(sys.argv) < 2:
    print "Invalid param, tell which url to crawl."
    sys.exit(0)

if len(sys.argv) >2:
    depth=int(sys.argv[2])

domain_name=sys.argv[1]

rls=urlparse(domain_name)
ll_file=open(dir_cur+rls.netloc+'.urls',"w",0)

print "Parsing domain:%s --depth:%d" %(domain_name,depth)


link_re = re.compile(r'href="(.*?)"')

def crawl(url, maxlevel):
    #check domain
    urls.append(url)

    if not url.startswith(domain_name):
        print "[Skip] %s domian missmatch!" % (url)
        return False

   
    if maxlevel == 0:
        return False
    
    ll_file.write(url+"\n")
    # Get the webpage
    req = requests.get(url)

    # Check if successful
    if(req.status_code != 200):
        print "[Error] %s got %d status" %(url,req.status_code)
        return False

    # Find and follow all the links
    links = link_re.findall(req.text)
    for link in links:
        if link.startswith('/') or link.startswith('#'):
            link=domain_name+link
        if link not in urls:
            crawl(link, maxlevel - 1)

crawl(sys.argv[1], depth)

print "Spider Scrapper finished."

