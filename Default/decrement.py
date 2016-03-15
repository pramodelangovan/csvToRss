'''
Created on Mar 11, 2016

@author: Sylvia Navachudar
'''
import datetime

''' 

function to get today's date

date +/- datetime.timedelta(days=i)

    where date is a date object,
    + to add days
    - to subtract days
    datetime.timedelta(days=i) to add number of days, can be used to month and year by replacing keyword day
        where i is the unit 

'''
s = datetime.datetime.today() 

#declaring lists
#re initiating 
date_array = list()
sorted_array = list()

#creating days list by subtracting 0 to 6 days with i
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
