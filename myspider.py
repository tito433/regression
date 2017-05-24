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
exclude_urls=(".js",".css")

dir_cur=os.path.dirname(os.path.realpath(__file__))+"/"
if len(sys.argv) < 2:
    print "Insufficient param, tell which file to load as url lines."
    sys.exit(0)

domain_name=sys.argv[1]
rls=urlparse(domain_name)
domain=rls.netloc
if len(sys.argv) >2:
    domain=sys.argv[2]

dir_output=dir_cur+domain+"/"
if not os.path.exists(dir_output):
    os.mkdir(dir_output)

if len(sys.argv) >3:
    depth=int(sys.argv[3])

ll_file=open(dir_output+domain+".urls","w",0)





print "Parsing domain:%s --depth:%d" %(domain_name,depth)


link_re = re.compile(r'href="(.*?)"')

def isValid(url):
    if not url.startswith(domain_name):
        print "[Skip] %s domian missmatch!" % (url)
        return False
    if url.endswith(exclude_urls):
        print "[Skip] %s forbidden files!" % (url)
        return False
    return True


def cleanUP(url):
    hChar=url.find('#')
    if hChar !=-1:
       url=url[:hChar]
    return url
     
def crawl(url, maxlevel):
    #check domain
    if not isValid(url):
        return False

    urls.append(url)
    print "[Load] %s" %(url)
    ll_file.write(url+"\n")
    if maxlevel>0:
        # Get the webpage
        resp = requests.get(url)
        # Check if successful
        if(resp.status_code != 200):
            print "[Error] %s got %d status" %(url,resp.status_code)
            return False
        # Find and follow all the links
        links = link_re.findall(resp.text)
        for link in links:
            if link.startswith('/'):
                link=domain_name+link
            link=cleanUP(link)
            if link not in urls:
                crawl(link, maxlevel - 1)

crawl(sys.argv[1], depth)

print "Spider Scrapper finished."

