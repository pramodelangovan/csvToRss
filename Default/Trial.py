'''
Created on Mar 8, 2016

@author: Sylvia Navachudar
'''
import csv
import datetime

f= open('C:\\Users\\Sylvia Navachudar\\Desktop\\Mock.csv')
reader = csv.reader(f)
s = datetime.datetime.today() 

#declaring lists
#re initiating 
date_array = list()
sorted_array = list()
for row in reader:
    for i in range(0,3):
        date_array.append(s - datetime.timedelta(days=i))

#getting the length of the array dynamically
c = int(len(date_array))

#Comparing the date to find the max than today + 1 (Yesterday)
for i in range(0,c):
    if date_array[i] <= s - datetime.timedelta(days=1):
        sorted_array.append(date_array[i])

#getting the length of the array dynamically
d = int(len(sorted_array))

#Printing the date array in mm/dd/yyyy
for i in range(0,d):
    print(sorted_array[i].strftime('%m/%d/%Y'))

print(row)
