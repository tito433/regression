import re
import sys
import os
from urlparse import urlparse

string='20,http://globalblue.test.globalblue.cue.cloud/destinations/finland/'
pattern = re.compile("^(\d+),(.*)$")
idx,url=[x for x in pattern.split(string) if x]

print "id:%s, url:%s" %(idx,url)