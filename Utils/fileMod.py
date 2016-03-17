'''
Created on Mar 17, 2016

@author: pramood
'''
import urllib 
import Utils.csvMod as Csv

from urllib.request import urlopen

class FileOp:

    def readfile(self, url):
        data = urlopen(url) 
        CsvOp = Csv.CsvParser()
        CsvOp.csvIm(data) 