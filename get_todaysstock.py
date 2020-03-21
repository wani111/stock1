from balancesheet_itooza import *
from time_folder import pathfolder, datetime

MakeDataFrameforDisplay(MakeDataStorage('바텍'))

df = pd.DataFrame(DataList)
df.to_html(pathfolder + '/today' + datetime + '.html')
writer = pd.ExcelWriter(pathfolder + '/today' +datetime + '.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='today')
writer.save()

