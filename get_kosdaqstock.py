from balancesheet_itooza import *
from companycode import *
import time
import pandas as pd
from time_folder import *
from multiprocessing import Pool  # Pool import하기
import sys
from run import *
import json

log = open('log.txt', 'w', encoding='utf-8')
#     print(bs, file=bstable)

start = time.time()

# for idx, items in kosdaq_stock_code.iterrows():
#     try:
#         MakeDataStorage(items['Name'])
#     except:
#         print(f"Fail... {items['Name']}")
#         continue
#     finally:
#         df = pd.DataFrame(DataList)
#         df.to_html(pathfolder + '/kosdaq' + datetime + '.html')
#         writer = pd.ExcelWriter(pathfolder + '/kosdaq' + datetime + '.xlsx', engine='xlsxwriter')
#         df.to_excel(writer, sheet_name='kosdaq')

#         workbook = writer.book
#         worksheet = writer.sheets['kosdaq']
#         worksheet.autofilter('A1:Y1')

#         # Light red fill with dark red text.
#         format1 = workbook.add_format({'bg_color':   '#FFC7CE',
#                                        'font_color': '#9C0006'})

#         # Light yellow fill with dark yellow text.
#         format2 = workbook.add_format({'bg_color':   '#FFEB9C',
#                                        'font_color': '#9C6500'})

#         # Green fill with dark green text.
#         format3 = workbook.add_format({'bg_color':   '#C6EFCE',
#                                        'font_color': '#006100'})

#         worksheet.conditional_format('T2:Y2000', {'type':     'cell',
#                                                   'criteria': 'greater than',
#                                                   'value':    24,
#                                                   'format':   format3})

#         worksheet.conditional_format('T2:Y2000', {'type':     'cell',
#                                                   'criteria': 'between',
#                                                   'minimum': 16,
#                                                   'maximum': 24,
#                                                   'format':   format1})

#         worksheet.conditional_format('T2:Y2000', {'type':     'cell',
#                                                   'criteria': 'between',
#                                                   'minimum': 8,
#                                                   'maximum': 16,
#                                                   'format':   format2})

#         writer.save()

lists = kosdaq_stock_code["Name"].tolist()
run_multiprocess(lists)
df = pd.DataFrame(list(DataList))
df.to_html(pathfolder + '/kosdaq' + datetime + '.html')
df.to_html(border=0, classes='display compact', table_id='stocktable', justify='center', buf=pathfolder2 + '/kosdaq' + datetime + '.html')
writer = pd.ExcelWriter(pathfolder + '/kosdaq' + datetime + '.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='kosdaq')

df.insert(0, 'rank', 1)
result = df.to_json(orient='split', index=False, indent=4)
parsed = json.loads(result)
del parsed['columns']
# print(f'{parsed}, {type(parsed)}')
with open(pathfolder2 + '/Kosdaq' + datetime + '.json', 'w') as f:
    json.dump(parsed, f)
with open(pathfolder3 + 'Kosdaq.json', 'w') as f:
    json.dump(parsed, f)
tm = time.localtime()
string = time.strftime('%Y-%m-%d %H:%M', tm)
with open(pathfolder3 + 'kosdaq_lastupdate.txt', 'w') as f:
    f.write(string)

workbook = writer.book
worksheet = writer.sheets['kosdaq']
worksheet.autofilter('A1:Y1')

# Light red fill with dark red text.
format1 = workbook.add_format({'bg_color':   '#FFC7CE',
                               'font_color': '#9C0006'})

# Light yellow fill with dark yellow text.
format2 = workbook.add_format({'bg_color':   '#FFEB9C',
                               'font_color': '#9C6500'})

# Green fill with dark green text.
format3 = workbook.add_format({'bg_color':   '#C6EFCE',
                               'font_color': '#006100'})

worksheet.conditional_format('T2:Y2000', {'type':     'cell',
                                          'criteria': 'greater than',
                                          'value':    24,
                                          'format':   format3})

worksheet.conditional_format('T2:Y2000', {'type':     'cell',
                                          'criteria': 'between',
                                          'minimum': 16,
                                          'maximum': 24,
                                          'format':   format1})

worksheet.conditional_format('T2:Y2000', {'type':     'cell',
                                          'criteria': 'between',
                                          'minimum': 8,
                                          'maximum': 16,
                                          'format':   format2})

writer.save()
print(f"time : {time.time() - start}s")  # 현재시각 - 시작시간 = 실행 시간

log.close()
