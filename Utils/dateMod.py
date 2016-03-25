'''
Created on Mar 16, 2016

@author:  Sylvia Navachudar
'''
import datetime

class getdate:
    day = None 

    def __init__(self):
        self.day = datetime.datetime.today()
        
    def getdate(self, mod, inc):
        if(mod == 'add'):
            return self.day + datetime.timedelta(days=inc)
        else:
            if(mod== 'sub'):
                return self.day - datetime.timedelta(days=inc)