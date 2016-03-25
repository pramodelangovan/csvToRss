'''
Created on Mar 23, 2016

@author: Sylvia Navachudar
'''
from ftplib import FTP
import ftplib


def Main():
    try :
        ftplib.FTP.port=81
        ftp = FTP('10.91.1.97')
        ftp.login('soujanya', '')
        print("connected")
        file = ftp.dir()
    except:
        print("error Connection")   

if __name__ == '__main__' :
    Main()