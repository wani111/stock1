from balancesheet_itooza import *
from time_folder import pathfolder, datetime
import time
from multiprocessing import Pool  # Pool import하기

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

lists = ['엠씨넥스', '한국금융지주', '케이씨', '아세아제지', '에스에이엠티', '월덱스', '인탑스', '제노레이', '삼성전자', 'SK하이닉스']
# freeze_support()
pool = Pool(processes=8)  # 4개의 프로세스를 사용합니다.
pool.map(MakeDataStorage, lists)  # get_contetn 함수를 넣어줍시다.
pool.close()
pool.join()

df.to_html(pathfolder + '/MyStock' + datetime + '.html')
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
