'''
Created on Mar 17, 2016

@author: Sylvia Navachudar
'''
import urllib
from urllib.request import urlopen


class FileOp:

    def readfile(self, url):
        data = urlopen(url) 
        next(data)
        next(data)
        next(data)
        next(data)
        next(data)
        next(data)
        for i, line in enumerate(data):
            print('line{} = {}'.format(i,line))
            
