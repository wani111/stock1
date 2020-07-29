from balancesheet_itooza import *
from time_folder import pathfolder, datetime
from multiprocessing import Pool  # Pool import하기

lists = ['KG케미칼',
         '동남합성',
         '미원상사',
         '미원에스씨',
         '미원화학',
         '백광산업',
         '한솔케미칼',
         '영풍제지',
         'DB하이텍',
         '해성디에스',
         '한진중공업홀딩스',
         'JW생명과학',
         '대원제약',
         '케이씨텍',
         '삼양식품',
         '샘표식품',
         '크라운제과',
         '시디즈',
         'SK디앤디',
         '다우기술',
         '더블유게임즈',
         '에이리츠',
         '두산인프라코어',
         'S&T홀딩스',
         '대상홀딩스',
         '미원홀딩스',
         '한국콜마홀딩스',
         '동부건설',
         '코오롱글로벌',
         '태영건설']


pool = Pool(processes=8)  # 4개의 프로세스를 사용합니다.
pool.map(MakeDataStorage, lists)  # get_contetn 함수를 넣어줍시다.
pool.close()
pool.join()

df = pd.DataFrame(list(DataList))
df.to_html(pathfolder + '/today' + datetime + '.html')
writer = pd.ExcelWriter(pathfolder + '/today' + datetime + '.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='today')

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
