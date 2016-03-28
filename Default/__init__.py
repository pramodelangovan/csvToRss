import Utils.dateMod  as dateutils
import Utils.fileMod as fm

day = dateutils.getdate()
#print(day.getdate('sub', 3))


fil = fm.FileOp()
fil.ftpfile('http://localhost/app/mock.csv')

