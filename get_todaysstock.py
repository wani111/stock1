from balancesheet_itooza import *
from time_folder import *
from multiprocessing import Pool  # Pool import하기
import sys
from run import *
import time
import json

start = time.time()

lists = ['KG케미칼',
         '동남합성',
         '미원상사',
         '미원에스씨',
         '미원화학',
         '백광산업',
         '한솔케미칼',
         '영풍제지',
         ]

run_multiprocess(lists)

df = pd.DataFrame(list(DataList))
df = df[['name', 'value', 'TPy', 'ERy(%)', 'TP10', 'ER10(%)', 'ROE3', 'EPSy', 'BPSy', 'ROEy', 'EPSc', 'DPS(%)', 'PER', 'PBR', 'EX3', 'EXy']]
df.to_html(pathfolder + '/today' + datetime + '.html')
df.to_html(border=0, classes='display compact', table_id='stocktable', justify='center', buf=pathfolder2 + '/today' + datetime + '.html')


writer = pd.ExcelWriter(pathfolder + '/today' + datetime + '.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='today')

df.insert(0, 'rank', 1)
result = df.to_json(orient='split', index=False, indent=4)
parsed = json.loads(result)
del parsed['columns']
# print(f'{parsed}, {type(parsed)}')
with open(pathfolder2 + '/today' + datetime + '.json', 'w') as f:
    json.dump(parsed, f)
with open(pathfolder3 + 'today.json', 'w') as f:
    json.dump(parsed, f)


workbook = writer.book
worksheet = writer.sheets['today']
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
print(f"time : {time.time() - start}s")  # 현재시각 - 시작시간 = 실행 시
