from balancesheet_itooza import *
from companycode import *
import time
import pandas as pd
from time_folder import pathfolder, datetime

log = open('log.txt', 'w', encoding='utf-8')
  #     print(bs, file=bstable)

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

for idx, items in kosdaq_stock_code.iterrows() :
    try : MakeDataFrameforDisplay(MakeDataStorage(items['Name']))
    except : 
        print(f"Fail... {items['Name']}")
        continue
    finally :
        df = pd.DataFrame(DataList)
        df.to_html(pathfolder + '/kosdaq' + datetime + '.html')
        writer = pd.ExcelWriter(pathfolder + '/kosdaq' +datetime + '.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='kosdaq')
        
        workbook = writer.book
        worksheet = writer.sheets['kosdaq']
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
# MakeDataFrameforDisplay(MakeDataStorage('CJ CGV'))
# MakeDataFrameforDisplay(MakeDataStorage('CJ ENM'))



print(f"time : {time.time() - start}s")  # 현재시각 - 시작시간 = 실행 시간

log.close()  