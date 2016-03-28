'''
Created on Mar 17, 2016

@author: pramood
'''
import csv
from io import StringIO
import itertools
import PyRSS2Gen
import datetime


class CsvParser:
    
    def csvIm(self, Fcsv):
        csvf = StringIO(Fcsv.decode())
        data = csv.reader(csvf)
        
        
        rss = PyRSS2Gen.RSS2(title = "Sylvia's csv to RSS project",
        link = "http://localhost/",
        description = "This project will convert CSV to RSS",
        lastBuildDate = datetime.datetime.now(),
        items=[])
        for row in itertools.islice(data, 0, 99999):
            item = PyRSS2Gen.RSSItem(
                   title =str(row[1]),
                   link = str(row[2]),
                   description = row[5]+" "+row[6]+" "+row[7]+" "+row[8]+" "+row[9]+" "+row[10]+" "+row[11]+" "+row[12]+" ",
                   pubDate = str(row[3]+ " to "+row[4]),
                   )
            rss.items.append(item)
        
        rss.write_xml(open("D:\Dev\Projects\pyrss2gen.xml", "w"),)
        
        

#Fcsv.read().decode('utf-8').splitlines()

# data = []
# with codecs.open('sorted.de.word.unigrams', 'r') as f:
#     for line in f:
#          data.append(line)
