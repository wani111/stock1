from balancesheet_itooza import *
from time_folder import pathfolder, datetime
import time

start = time.time()

kospipathfolder = './financedata/' + datetime +'/kospi/'
if(not os.path.isdir(kospipathfolder)):
  os.mkdir(kospipathfolder)
  os.mkdir(kospipathfolder + '/Annualized')
  os.mkdir(kospipathfolder + '/Year')
  os.mkdir(kospipathfolder + '/Annualized/csv')
  os.mkdir(kospipathfolder + '/Annualized/html')
  os.mkdir(kospipathfolder + '/Year/csv')
  os.mkdir(kospipathfolder + '/Year/html')
  
MakeDataFrameforDisplay(MakeDataStorage('엠씨넥스'))
MakeDataFrameforDisplay(MakeDataStorage('한국금융지주'))
MakeDataFrameforDisplay(MakeDataStorage('케이씨'))
MakeDataFrameforDisplay(MakeDataStorage('아세아제지'))
MakeDataFrameforDisplay(MakeDataStorage('에스에이엠티'))
MakeDataFrameforDisplay(MakeDataStorage('월덱스'))
MakeDataFrameforDisplay(MakeDataStorage('S&K폴리텍'))
MakeDataFrameforDisplay(MakeDataStorage('인탑스'))
MakeDataFrameforDisplay(MakeDataStorage('제노레이'))
MakeDataFrameforDisplay(MakeDataStorage('삼성전자'))
MakeDataFrameforDisplay(MakeDataStorage('SK하이닉스'))


df = pd.DataFrame(DataList)
df.to_html(pathfolder + '/MyStock' + datetime + '.html')
writer = pd.ExcelWriter(pathfolder + '/MyStock' +datetime + '.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='MyStock')

workbook = writer.book
worksheet = writer.sheets['MyStock']
worksheet.autofilter('A1:X1')

# Light red fill with dark red text.
format1 = workbook.add_format({'bg_color':   '#FFC7CE',
                               'font_color': '#9C0006'})

# Light yellow fill with dark yellow text.
format2 = workbook.add_format({'bg_color':   '#FFEB9C',
                               'font_color': '#9C6500'})

# Green fill with dark green text.
format3 = workbook.add_format({'bg_color':   '#C6EFCE',
                               'font_color': '#006100'})

worksheet.conditional_format('T2:X2000', {'type':     'cell',
                                        'criteria': 'greater than',
                                        'value':    24,
                                        'format':   format3})

worksheet.conditional_format('T2:X2000', {'type':     'cell',
                                        'criteria': 'between',
                                        'minimum' : 16,
                                        'maximum' : 24,
                                        'format':   format1})

worksheet.conditional_format('T2:X2000', {'type':     'cell',
                                        'criteria': 'between',
                                        'minimum' : 8,
                                        'maximum' : 16,
                                        'format':   format2})
writer.save()