from balancesheet_itooza import *
from time_folder import pathfolder, datetime

MakeDataFrameforDisplay(MakeDataStorage('삼성전자'))
MakeDataFrameforDisplay(MakeDataStorage('SK하이닉스'))
MakeDataFrameforDisplay(MakeDataStorage('한양이엔지'))
MakeDataFrameforDisplay(MakeDataStorage('프로텍'))
MakeDataFrameforDisplay(MakeDataStorage('월덱스'))
MakeDataFrameforDisplay(MakeDataStorage('한국알콜'))
MakeDataFrameforDisplay(MakeDataStorage('엠씨넥스'))
MakeDataFrameforDisplay(MakeDataStorage('탑엔지니어링'))
MakeDataFrameforDisplay(MakeDataStorage('케이씨'))
MakeDataFrameforDisplay(MakeDataStorage('인탑스'))
MakeDataFrameforDisplay(MakeDataStorage('제노레이'))
MakeDataFrameforDisplay(MakeDataStorage('아바코'))
MakeDataFrameforDisplay(MakeDataStorage('에스에이엠티'))
MakeDataFrameforDisplay(MakeDataStorage('아주캐피탈'))
MakeDataFrameforDisplay(MakeDataStorage('제우스'))
MakeDataFrameforDisplay(MakeDataStorage('코미코'))
MakeDataFrameforDisplay(MakeDataStorage('에스티아이'))
MakeDataFrameforDisplay(MakeDataStorage('유니테스트'))
MakeDataFrameforDisplay(MakeDataStorage('지누스'))
MakeDataFrameforDisplay(MakeDataStorage('바텍'))



df = pd.DataFrame(DataList)
df.to_html(pathfolder + '/MyStock' + datetime + '.html')
writer = pd.ExcelWriter(pathfolder + '/MyStock' +datetime + '.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='MyStock')
writer.save()