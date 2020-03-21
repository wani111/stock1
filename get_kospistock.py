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

for idx, items in kospi_stock_code.iterrows() :
    try : MakeDataFrameforDisplay(MakeDataStorage(items['Name']))
    except : 
        print(f"Fail... {items['Name']}")
        break
    finally :
        df = pd.DataFrame(DataList)
        df.to_html(pathfolder + '/kospi' + datetime + '.html')
        writer = pd.ExcelWriter(pathfolder + '/kospi' +datetime + '.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='kospi')
        writer.save()
# MakeDataFrameforDisplay(MakeDataStorage('CJ CGV'))
# MakeDataFrameforDisplay(MakeDataStorage('CJ ENM'))



print(f"time : {time.time() - start}s")  # 현재시각 - 시작시간 = 실행 시간

log.close()  