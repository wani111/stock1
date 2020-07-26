from balancesheet_itooza import *
from companycode import *
import time
import pandas as pd
from time_folder import pathfolder, datetime
from multiprocessing import Pool  # Pool import하기

log = open('log.txt', 'w', encoding='utf-8')
#     print(bs, file=bstable)

start = time.time()

for idx, items in kospi_stock_code.iterrows():
    try:
        MakeDataStorage(items['Name'])
    except:
        print(f"Fail... {items['Name']}")
        continue
    finally:
        df = pd.DataFrame(DataList)
        df.to_html(pathfolder + '/kospi' + datetime + '.html')
        writer = pd.ExcelWriter(pathfolder + '/kospi' + datetime + '.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='kospi')

        workbook = writer.book
        worksheet = writer.sheets['kospi']
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
                                                  'minimum': 16,
                                                  'maximum': 24,
                                                  'format':   format1})

        worksheet.conditional_format('T2:X2000', {'type':     'cell',
                                                  'criteria': 'between',
                                                  'minimum': 8,
                                                  'maximum': 16,
                                                  'format':   format2})

        writer.save()


# lists = stock_data["Name"].tolist()
# pool = Pool(processes=8)  #
# pool.map(MakeDataStorage, lists)  #
# pool.close()
# pool.join()


df = pd.DataFrame(DataList)
df.to_html(pathfolder + '/kospi' + datetime + '.html')
writer = pd.ExcelWriter(pathfolder + '/kospi' + datetime + '.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='kospi')

workbook = writer.book
worksheet = writer.sheets['kospi']
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
                                          'minimum': 16,
                                          'maximum': 24,
                                          'format':   format1})

worksheet.conditional_format('T2:X2000', {'type':     'cell',
                                          'criteria': 'between',
                                          'minimum': 8,
                                          'maximum': 16,
                                          'format':   format2})

writer.save()

print(f"time : {time.time() - start}s")  # 현재시각 - 시작시간 = 실행 시간

log.close()
