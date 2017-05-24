import re
import sys

url='www.globalblue.com'
m = re.search('([a-z0-9|-]+\.)*([a-z0-9|-]+\.[a-z]+)',url)
pos=0
if len(sys.argv) >= 2:
	pos=int(sys.argv[1])
	print "Pos:%d" % (pos)

print m.group(pos)