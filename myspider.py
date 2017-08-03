import requests
import re
import os
import sys
import shutil
import os.path
from urlparse import urlparse
import csv




#print urlparse(sys.argv[1])
if len(sys.argv)==1:
	print "Params are: <domain> <test> <depth>"
	sys.exit(0)

depth=0
urls=[]
allowed_domain=['globalblue.cn','globalblue.ru','globalblue.zh','globalblue.com',
	'globalblue.cue.cloud']

exclude_file_ext=(".js",".css",".ico",)

dir_cur=os.path.dirname(os.path.realpath(__file__))
if len(sys.argv) < 2:
	print "Insufficient param, tell which file to load as url lines."
	sys.exit(0)

domain_name=sys.argv[1]
test_name='test' if len(sys.argv) <3 else sys.argv[2] 
rls=urlparse(domain_name)
if rls.scheme =='':
	domain_name="http://"+domain_name
allowed_domain+=(str(rls.netloc),)

dir_output=os.path.join(dir_cur,test_name)

if not os.path.exists(dir_output):
	os.mkdir(dir_output)

if len(sys.argv) >3:
	depth=int(sys.argv[3])

++depth

file_urls_path=os.path.join(dir_output,test_name+".urls")
if os.path.isfile(file_urls_path):
	urls = [line.rstrip('\n') for line in open(file_urls_path)]

file_csv=open(os.path.join(dir_output,test_name+".csv"),"wb",0)

logwriter = csv.writer(file_csv, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
print "Crawling domain:%s --depth:%d" %(rls.netloc,depth)
logwriter.writerow(["TYPE","URL","PARENT"])

link_re = re.compile(r'href="((?!#).*?)"')

def isValid(url):
	rls=urlparse(url)
	if not any(s for s in allowed_domain if  str(rls.netloc).endswith(s)) or str(rls.path).endswith(exclude_file_ext):
		return False
	return True

def crawl(url, maxlevel,parent=False):
	if not parent:
		parent=url

	if maxlevel<0 or url in urls:
		return False

	urls.append(url)
	f = open(file_urls_path, 'a+', 0)
	f.write(url+"\n")
	f.close()
	
	print "Crawling: ",url, " Depth:",maxlevel

	try:
		resp = requests.get(url, verify=False, timeout=20)
		if(resp.status_code != 200):
			logwriter.writerow([resp.status_code,url,parent])
			file_csv.flush()
			os.fsync(file_csv.fileno())
		else:
			for link in link_re.findall(resp.text):
				if link.startswith('/'):
					link=domain_name+link
				if link.startswith('?'):
					link=url+link
				if isValid(link) and link not in urls:
					crawl(link, maxlevel - 1,url)

	except Exception as e:
		logwriter.writerow(["Error",url,parent])
		file_csv.flush()
		os.fsync(file_csv.fileno())
		

crawl(domain_name, depth)
file_csv.close()

print "Spider Scrapper finished. Total url fetched:%d" %(len(urls))

