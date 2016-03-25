'''
Created on Mar 17, 2016

@author: Sylvia Navachudar
'''
import urllib 
import Utils.csvMod as Csv

from urllib.request import urlopen


class FileOp:

    def readfile(self, url):
        data = urlopen(url) 
<<<<<<< .merge_file_a05012
        next(data)
        next(data)
        next(data)
        next(data)
        next(data)
        next(data)
        for i, line in enumerate(data):
            print('line{} = {}'.format(i,line))
            
=======
        CsvOp = Csv.CsvParser()
        CsvOp.csvIm(data) 
>>>>>>> .merge_file_a04432
