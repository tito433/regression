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


if len(sys.argv) < 2:
    print "Invalid param, tell which url to crawl."
    sys.exit(0)


def getDomain(url):
    dd=urlparse(url)
    m = re.search('([a-z0-9|-]+\.)*([a-z0-9|-]+\.[a-z]+)',dd.netloc)
    ret=dd.netloc
    if m and m.group(2):
        ret=m.group(2)
    return  ret


orgin_domain=sys.argv[1]
domain_name=getDomain(sys.argv[1])


ll_file=open(dir_cur+domain_name+'.urls',"w")

print "Parsing domain:"+domain_name


link_re = re.compile(r'href="(.*?)"')

def crawl(url, maxlevel):
    #check domain
    cDom=getDomain(url)

    if cDom == '':
        url=orgin_domain+url
    elif  cDom !=  domain_name:
        print "[Skip] %s (%s,%s) domian missmatch!" % (url,cDom,domain_name)
        return False

    ll_file.write(url+"\n")
    if maxlevel == 0:
        return False
    
    oUrl=urlparse(url)
    if oUrl.scheme =='https':
        print "[SKIP] %s reason: https not supported."
        return False

    # Get the webpage
    req = requests.get(url)

    # Check if successful
    if(req.status_code != 200):
        print "[Error] %s got %d status" %(url,req.status_code)
        return False

    # Find and follow all the links
    links = link_re.findall(req.text)
    for link in links:
        crawl(link, maxlevel - 1)

crawl(sys.argv[1], 10)

print "Spider Scrapper finished."

