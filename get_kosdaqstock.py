from balancesheet_itooza import *
from companycode import stock_code
import time
import pandas as pd

log = open('log.txt', 'w', encoding='utf-8')
  #     print(bs, file=bstable)

start = time.time()

for idx, items in kosdaq_stock_code.iterrows() :
    try : MakeDataFrameforDisplay(MakeDataStorage(items['Name']))
    except : 
        print(f"Fail... {items['Name']}")
        break
    finally :
        df = pd.DataFrame(DataList)
        df.to_html('./financedata/kosdaq.html')
        writer = pd.ExcelWriter('kosdaq.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='kosdaq')
        writer.save()
# MakeDataFrameforDisplay(MakeDataStorage('CJ CGV'))
# MakeDataFrameforDisplay(MakeDataStorage('CJ ENM'))



print(f"time : {time.time() - start}s")  # 현재시각 - 시작시간 = 실행 시간

log.close()  