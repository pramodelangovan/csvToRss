'''
Created on Mar 10, 2016

@author: Sylvia Navachudar
'''
import csv

f = open('C:\\Users\\Sylvia Navachudar\\Desktop\\Mock.csv')
reader = csv.reader(f)
data = []
for row in reader:
    print(row)