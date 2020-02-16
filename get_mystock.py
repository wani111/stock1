from balancesheet_itooza import *

MakeDataFrameforDisplay(MakeDataStorage('삼성전자'))
MakeDataFrameforDisplay(MakeDataStorage('SK하이닉스'))
MakeDataFrameforDisplay(MakeDataStorage('카카오'))
MakeDataFrameforDisplay(MakeDataStorage('한양이엔지'))
MakeDataFrameforDisplay(MakeDataStorage('프로텍'))
MakeDataFrameforDisplay(MakeDataStorage('월덱스'))
MakeDataFrameforDisplay(MakeDataStorage('한국알콜'))
MakeDataFrameforDisplay(MakeDataStorage('아세아제지'))

df = pd.DataFrame(DataList)
df.to_html('./financedata/my.html')
writer = pd.ExcelWriter('stock.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='my')
writer.save()