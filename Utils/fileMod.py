'''
Created on Mar 17, 2016

@author: Sylvia Navachudar
'''
import urllib 
import Utils.csvMod as Csv
from ftplib import FTP
import ftplib


from urllib.request import urlopen


class FileOp:
   
    def readfile(self, url):
        data = urlopen(url)
        Rdata = data.read()
        

        CsvOp = Csv.CsvParser()
        CsvOp.csvIm(Rdata) 


    
    def ftpfile(self, url):
#         try :
            #ftplib.FTP.port=81
            #ftp = FTP('10.91.1.97')
            #ftp.login('soujanya', '')
            #print("connected")
        self.readfile(url)
#         except:
#             print("error Connection")   

    
    