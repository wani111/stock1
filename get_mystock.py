from balancesheet_itooza import *
from time_folder import pathfolder, pathfolder2, datetime
import time
from multiprocessing import Pool  # Pool import하기
import sys
from run import *
start = time.time()


# MakeDataStorage('엠씨넥스')
# MakeDataStorage('한국금융지주')
# MakeDataStorage('케이씨')
# MakeDataStorage('아세아제지')
# MakeDataStorage('에스에이엠티')
# MakeDataStorage('월덱스')
# MakeDataStorage('인탑스')
# MakeDataStorage('제노레이')
# MakeDataStorage('삼성전자')
# MakeDataStorage('SK하이닉스')

# lists = ['엠씨넥스', '한국금융지주', '케이씨', '아세아제지', '에스에이엠티', '월덱스', '인탑스', '제노레이', '삼성전자', 'SK하이닉스']
# lists = ['CJ CGV', 'CJ씨푸드', 'DB손해보험', 'F&F', 'HDC현대산업개발', 'KB금융', 'KC코트렐', 'KPX홀딩스', 'LG하우시스', 'LS']

lists = ['GST',
         'KCI',
         'KG ETS',
         'KG이니시스',
         '고려신용정보',
         '나이스디앤비',
         '동성화인텍',
         '비엠티',
         '비츠로테크',
         '서린바이오',
         '어보브반도체',
         '에스티아이',
         '에이치시티',
         '오이솔루션',
         '와이엔텍',
         '윈스',
         '이엔에프테크놀로지',
         '이엠넷',
         '이크레더블',
         '인선이엔티',
         '제이티',
         '케이엠',
         '케이엠더블유',
         '코미코',
         '클래시스',
         '토탈소프트',
         '피앤이솔루션',
         '한국기업평가']

run_multiprocess(lists)

df = pd.DataFrame(list(DataList))
df.to_html(pathfolder + '/MyStock' + datetime + '.html')
df.to_html(border=0, classes='display compact', table_id='stocktable', justify='center', buf=pathfolder2 + '/MyStock' + datetime + '.html')
writer = pd.ExcelWriter(pathfolder + '/MyStock' + datetime + '.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='MyStock')

workbook = writer.book
worksheet = writer.sheets['MyStock']
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
