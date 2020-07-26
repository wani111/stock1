from balancesheet_itooza import *
from time_folder import pathfolder, datetime

MakeDataFrameforDisplay(MakeDataStorage('샘표'))
MakeDataFrameforDisplay(MakeDataStorage('한섬'))
MakeDataFrameforDisplay(MakeDataStorage('포스코 ICT'))
MakeDataFrameforDisplay(MakeDataStorage('다우기술'))
MakeDataFrameforDisplay(MakeDataStorage('케이씨'))
MakeDataFrameforDisplay(MakeDataStorage('다우데이타'))
MakeDataFrameforDisplay(MakeDataStorage('파세코'))
MakeDataFrameforDisplay(MakeDataStorage('한일네트웍스'))
MakeDataFrameforDisplay(MakeDataStorage('KG모빌리언스'))
MakeDataFrameforDisplay(MakeDataStorage('고려신용정보'))
MakeDataFrameforDisplay(MakeDataStorage('한국정보인증'))
MakeDataFrameforDisplay(MakeDataStorage('인선이엔티'))
MakeDataFrameforDisplay(MakeDataStorage('GST'))
MakeDataFrameforDisplay(MakeDataStorage('대상홀딩스'))
MakeDataFrameforDisplay(MakeDataStorage('차바이오텍'))
MakeDataFrameforDisplay(MakeDataStorage('청담러닝'))
MakeDataFrameforDisplay(MakeDataStorage('케이씨에스'))
MakeDataFrameforDisplay(MakeDataStorage('지엔씨에너지'))
MakeDataFrameforDisplay(MakeDataStorage('KMH'))
MakeDataFrameforDisplay(MakeDataStorage('현대에이치씨엔'))
MakeDataFrameforDisplay(MakeDataStorage('윈스'))
MakeDataFrameforDisplay(MakeDataStorage('그린플러스'))
MakeDataFrameforDisplay(MakeDataStorage('마니커에프앤지'))
MakeDataFrameforDisplay(MakeDataStorage('콜마비앤에이치'))
MakeDataFrameforDisplay(MakeDataStorage('미투온'))
MakeDataFrameforDisplay(MakeDataStorage('엑셈'))
MakeDataFrameforDisplay(MakeDataStorage('한솔제지'))
MakeDataFrameforDisplay(MakeDataStorage('소프트캠프'))
MakeDataFrameforDisplay(MakeDataStorage('디알젬'))
MakeDataFrameforDisplay(MakeDataStorage('디앤씨미디어'))
MakeDataFrameforDisplay(MakeDataStorage('인산가'))
MakeDataFrameforDisplay(MakeDataStorage('태평양물산'))
MakeDataFrameforDisplay(MakeDataStorage('광동제약'))
MakeDataFrameforDisplay(MakeDataStorage('더존비즈온'))
MakeDataFrameforDisplay(MakeDataStorage('동화기업'))
MakeDataFrameforDisplay(MakeDataStorage('NICE평가정보'))
MakeDataFrameforDisplay(MakeDataStorage('엠게임'))
MakeDataFrameforDisplay(MakeDataStorage('대한제강'))
# MakeDataFrameforDisplay(MakeDataStorage('효성ITX'))
MakeDataFrameforDisplay(MakeDataStorage('네오위즈'))
MakeDataFrameforDisplay(MakeDataStorage('제노레이'))
MakeDataFrameforDisplay(MakeDataStorage('이엠넷'))
MakeDataFrameforDisplay(MakeDataStorage('시디즈'))
MakeDataFrameforDisplay(MakeDataStorage('비즈니스온'))
MakeDataFrameforDisplay(MakeDataStorage('녹십자웰빙'))
# MakeDataFrameforDisplay(MakeDataStorage('브릿지바이오테라퓨틱스'))
MakeDataFrameforDisplay(MakeDataStorage('송원산업'))
MakeDataFrameforDisplay(MakeDataStorage('율촌화학'))
# MakeDataFrameforDisplay(MakeDataStorage('한국프랜지'))
MakeDataFrameforDisplay(MakeDataStorage('스페코'))
# MakeDataFrameforDisplay(MakeDataStorage('부산가스'))
MakeDataFrameforDisplay(MakeDataStorage('유비케어'))
MakeDataFrameforDisplay(MakeDataStorage('KG이니시스'))
MakeDataFrameforDisplay(MakeDataStorage('에이텍'))
MakeDataFrameforDisplay(MakeDataStorage('LG생활건강'))
MakeDataFrameforDisplay(MakeDataStorage('바이넥스'))
MakeDataFrameforDisplay(MakeDataStorage('인피니트헬스케어'))
MakeDataFrameforDisplay(MakeDataStorage('STX엔진'))
MakeDataFrameforDisplay(MakeDataStorage('드림텍'))
MakeDataFrameforDisplay(MakeDataStorage('오리콤'))
MakeDataFrameforDisplay(MakeDataStorage('뷰웍스'))
MakeDataFrameforDisplay(MakeDataStorage('미원화학'))
MakeDataFrameforDisplay(MakeDataStorage('매일유업'))
MakeDataFrameforDisplay(MakeDataStorage('대원제약'))
MakeDataFrameforDisplay(MakeDataStorage('삼양식품'))
MakeDataFrameforDisplay(MakeDataStorage('오뚜기'))
MakeDataFrameforDisplay(MakeDataStorage('서흥'))
MakeDataFrameforDisplay(MakeDataStorage('한솔케미칼'))
MakeDataFrameforDisplay(MakeDataStorage('나이스정보통신'))
MakeDataFrameforDisplay(MakeDataStorage('두산인프라코어'))
MakeDataFrameforDisplay(MakeDataStorage('에스앤에스텍'))
MakeDataFrameforDisplay(MakeDataStorage('티에스이'))
MakeDataFrameforDisplay(MakeDataStorage('엠아이텍'))
MakeDataFrameforDisplay(MakeDataStorage('코스맥스'))
MakeDataFrameforDisplay(MakeDataStorage('파마리서치프로덕트'))
MakeDataFrameforDisplay(MakeDataStorage('샘표식품'))


df = pd.DataFrame(DataList)
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
