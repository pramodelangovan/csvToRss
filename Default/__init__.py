import Utils.dateMod  as dateutils
import Utils.fileMod as fm

day = dateutils.getdate()
#print(day.getdate('add', 2))
#print(day.getdate('sub', 2))


fil = fm.FileOp()
fil.ftpfile('http://localhost/app/mock.csv')

