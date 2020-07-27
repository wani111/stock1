from datetime import datetime, timedelta
import os

dt_today = datetime.today()
#dt_today = datetime.strptime('2020-3-16 15:30:01', '%Y-%m-%d %H:%M:%S')
dt_modi = dt_today
# mon = 0, thu = 1, wed = 2 , thr = 3 , fri = 4, sat = 5, sun = 6
if(dt_today.weekday() == 0):
    if(dt_today.hour < 15):
        dt_modi = dt_today - timedelta(3)
    elif(dt_today.hour == 15 and dt_today.minute < 40):
        dt_modi = dt_today - timedelta(3)
elif(dt_today.weekday() >= 1 and dt_today.weekday() <= 4):
    if(dt_today.hour < 15):
        dt_modi = dt_today - timedelta(1)
    elif(dt_today.hour == 15 and dt_today.minute < 40):
        dt_modi = dt_today - timedelta(1)
elif(dt_today.weekday() == 5):
    dt_modi = dt_today - timedelta(1)
elif(dt_today.weekday() == 6):
    dt_modi = dt_today - timedelta(2)

# print(dt_today.weekday(), dt_modi.weekday())
# print(dt_today, dt_modi)


def Make_Folder(path):
    if(not os.path.isdir(path)):
        os.mkdir(path)


datetime = dt_modi.strftime('W%V_%A_%Y-%m-%d')

pathfolder = './financedata/' + datetime
print("Working for " + datetime)
Make_Folder(pathfolder)


kospipathfolder = './financedata/' + datetime + '/kospi/'

Make_Folder(kospipathfolder)
Make_Folder(kospipathfolder + '/Annualized')
Make_Folder(kospipathfolder + '/Year')
Make_Folder(kospipathfolder + '/Quarter')
Make_Folder(kospipathfolder + '/txt')
Make_Folder(kospipathfolder + '/Annualized/csv')
Make_Folder(kospipathfolder + '/Annualized/html')
Make_Folder(kospipathfolder + '/Year/csv')
Make_Folder(kospipathfolder + '/Year/html')
Make_Folder(kospipathfolder + '/Quarter/csv')
Make_Folder(kospipathfolder + '/Quarter/html')
