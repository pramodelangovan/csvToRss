'''
Created on Mar 14, 2016

@author: Sylvia Navachudar
'''
lines = list()
testAnswer = input('Press y if you want to enter more lines: ')
while testAnswer == 'y':
    line = input('Next line: ')
    lines.append(line)
    testAnswer = input('Press y if you want to enter more lines: ')

print('Your lines were:')
for line in lines:
    print(line)