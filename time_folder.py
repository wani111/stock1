from datetime import datetime, timedelta
import os

dt_today = datetime.today()
#dt_today = datetime.strptime('2020-3-16 15:30:01', '%Y-%m-%d %H:%M:%S')
dt_modi = dt_today
# mon = 0, thu = 1, wed = 2 , thr = 3 , fri = 4, sat = 5, sun = 6
if(dt_today.weekday() == 0) :
    if(dt_today.hour < 15) :
        dt_modi = dt_today - timedelta(3)
    elif(dt_today.hour == 15 and dt_today.minute < 40) :
         dt_modi = dt_today - timedelta(3)
elif(dt_today.weekday() >= 1 and dt_today.weekday() <= 4): 
    if(dt_today.hour < 15) :
        dt_modi = dt_today - timedelta(1)
    elif(dt_today.hour == 15 and dt_today.minute < 40) :
         dt_modi = dt_today - timedelta(1)   
elif(dt_today.weekday() == 5) :
    dt_modi = dt_today - timedelta(1)
elif(dt_today.weekday() == 6):
    dt_modi = dt_today - timedelta(2)
    
# print(dt_today.weekday(), dt_modi.weekday())
# print(dt_today, dt_modi)


datetime = dt_modi.strftime('W%V_%A_%Y-%m-%d')

pathfolder = './financedata/' + datetime
print("Working for " + datetime)
if(not os.path.isdir(pathfolder)):
	os.mkdir(pathfolder)