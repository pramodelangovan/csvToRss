import Utils.dateMod  as dateutils
import Utils.fileMod as fm


<<<<<<< .merge_file_a04328
day = dateutils.getdate()
print(day.getdate('add', 2))
print(day.getdate('sub', 2))

#http://localhost/app/sample.txt
filname = fm.FileOp()
filname.readfile('http://localhost/app/Mock.csv')
=======


fil = fm.FileOp()
fil.readfile('http://localhost/app/mock.csv')
>>>>>>> .merge_file_a04424
