from balancesheet_itooza import *
from time_folder import pathfolder

MakeDataFrameforDisplay(MakeDataStorage('바텍'))

df = pd.DataFrame(DataList)
df.to_html(pathfolder + '/today.html')
writer = pd.ExcelWriter(pathfolder + '/today.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='today')
writer.save()

