'''
Created on Mar 10, 2016

@author: Sylvia Navachudar
'''
import csv

csv.register_dialect('custom',
                    delimiter=',',
                    doublequote=True,
                    escapechar=None,
                    quotechar='"',
                    quoting=csv.QUOTE_MINIMAL,
                    skipinitialspace=False)
  
with open('C:\\Users\\Sylvia Navachudar\\Desktop\\Mock.csv') as ifile:
    data = csv.reader(ifile, dialect='custom')
    print ("<document>")
    for record in data:
        print ("<record>")
        for i, field in enumerate(record):
            print ("<field%s>" % i + field + "</field%s>" % i)
        print ("<record>")
print('</document>')