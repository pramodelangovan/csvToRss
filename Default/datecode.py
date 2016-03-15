'''
Created on Mar 10, 2016

@author: pramode

Sources:
http://stackoverflow.com/questions/16670601/how-to-perform-arithmetic-operation-on-a-date-in-python
http://importpython.blogspot.in/2009/12/how-to-get-todays-date-in-yyyymmdd.html
https://docs.python.org/2/library/datetime.html
'''
import datetime


''' 

function to get today's date

date +/- datetime.timedelta(days=i)

    where date is a date object,
    + to add days
    - to subract days
    datetime.timedelta(days=i) to add number of days, can be used to month and year by replacing keyword day
        where i is the unit 

'''
s = datetime.datetime.today() 
print('Today''s date is' + s.strftime('%m/%d/%Y'))
print()

#declaring lists
date_array = list()
sorted_array = list()

#creating days list by adding 0 to 6 days with i
for i in range(0,6):
    date_array.append(s + datetime.timedelta(days=i))

#getting the length of the array dynamically    
c = int(len(date_array))

#Comparing the date to find the max than today + 1 (Tomorrow) 
for i in range(0,c):
    if date_array[i] > s + datetime.timedelta(days=1):
        sorted_array.append(date_array[i])

#getting the length of the array dynamically        
d = int(len(sorted_array))
e = int(len(date_array))

for i in range(0,e):
    print('date by adding'+str(i))
    print(date_array[i].strftime('%m/%d/%Y'))
print()
#Printing the date array in mm/dd/yyyy
for i in range(0,d):
    print(sorted_array[i].strftime('%m/%d/%Y'))

#new line
print()

#re initiating 
date_array = list()
sorted_array = list()

#creating days list by subtracting 0 to 6 days with i
for i in range(0,6):
    date_array.append(s - datetime.timedelta(days=i))

#getting the length of the array dynamically
c = int(len(date_array))

#Comparing the date to find the max than today + 1 (Yesterday)
for i in range(0,c):
    if date_array[i] < s - datetime.timedelta(days=1):
        sorted_array.append(date_array[i])

#getting the length of the array dynamically
d = int(len(sorted_array))
e = int(len(date_array))

for i in range(0,e):
    print('date by subtracting'+str(i))
    print(date_array[i].strftime('%m/%d/%Y'))
print()
    
#Printing the date array in mm/dd/yyyy
for i in range(0,d):
    print(sorted_array[i].strftime('%m/%d/%Y'))
