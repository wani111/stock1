from balancesheet_itooza import *
from time_folder import pathfolder, datetime

MakeDataFrameforDisplay(MakeDataStorage('삼성전자'))
MakeDataFrameforDisplay(MakeDataStorage('S&K폴리텍'))
MakeDataFrameforDisplay(MakeDataStorage('클래시스'))
MakeDataFrameforDisplay(MakeDataStorage('파워로직스'))
MakeDataFrameforDisplay(MakeDataStorage('링네트'))
MakeDataFrameforDisplay(MakeDataStorage('상아프론테크'))
MakeDataFrameforDisplay(MakeDataStorage('엠씨넥스'))
MakeDataFrameforDisplay(MakeDataStorage('엘비세미콘'))





df = pd.DataFrame(DataList)
df.to_html(pathfolder + '/today' + datetime + '.html')
writer = pd.ExcelWriter(pathfolder + '/today' +datetime + '.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='today')

workbook = writer.book
worksheet = writer.sheets['today']
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

