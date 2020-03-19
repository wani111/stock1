from datetime import datetime
import os

datetime = datetime.today().strftime('%Y-%m-%d_%Hh')
#print(datetime)
pathfolder = './financedata/' + datetime
#print(pathfolder)
if(not os.path.isdir(pathfolder)):
	os.mkdir(pathfolder)