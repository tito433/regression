import requests
import re
import glob, os, sys
import shutil
import os.path


max_url_save=9999

dir_cur=os.path.dirname(os.path.realpath(__file__))+"/"
if len(sys.argv) < 2:
	print "Insufficient param, tell me which folder has the url file?"
	sys.exit(0)


dir_output=os.path.join(dir_cur,sys.argv[1])
if not os.path.exists(dir_output):
    print dir_output+" does not exist. I will exit now."
    sys.exit(0)

file_url=''

link_re = re.compile('article_([0-9]+)_([0-9]+)',re.IGNORECASE)

os.chdir(dir_output)
for file in glob.glob("*.urls"):
	file_url=file
	ll_file=open("%s.arts" % (os.path.basename(file)),"w",0)
	lines = [line.rstrip('\n') for line in open(file_url)]
	url_count=len(lines)
	print "Total url found:%d, will fetch:%d" %(url_count,min(url_count,max_url_save))
	url_count=min(url_count,max_url_save)

	for i in xrange(0, url_count):
		url=lines[i]
		try:
			resp = requests.get(url, verify=False, timeout=20)
			if(resp.status_code == 200):
				m=re.search('article_(\d+)_(\d+)',resp.text)
				if m:
					ll_file.write("%s,%s\n"%(m.group(1),url))
					ll_file.flush()
					print url

		except Exception as e:
			print e

print "Finish!"