import Utils.dateMod as dateutils
import Utils.fileMod as fm

#day = dateutils.getdate()
#print(day.getdate('add', 2))
#print(day.getdate('sub', 2))

#http://localhost/app/sample.txt

fil = fm.FileOp()
fil.readfile('http://localhost/app/sample.txt')