'''
Created on Mar 17, 2016

@author: pramood
'''
import csv

class CsvParser:
    
    def csvIm(self, Fcsv):
        reader = csv.reader(Fcsv.read().decode('utf-8'))
        for row in reader:
            print(row)
        print('here')
        