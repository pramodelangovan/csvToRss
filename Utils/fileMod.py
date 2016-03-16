'''
Created on Mar 17, 2016

@author: pramood
'''
import urllib
from urllib.request import urlopen

class FileOp:

    def readfile(self, url):
        data = urlopen(url) 
        