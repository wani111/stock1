from balancesheet_itooza import *

MakeDataFrameforDisplay(MakeDataStorage('후성'))
MakeDataFrameforDisplay(MakeDataStorage('LG헬로비전'))

df = pd.DataFrame(DataList)
df.to_html('./financedata/today.html')
writer = pd.ExcelWriter('stock.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='today')
writer.save()