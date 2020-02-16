from balancesheet_itooza import *
from companycode import *
import pandas as pd

def GetAllBalanceData() :
    for idx, items in stock_code.iterrows():
        if not os.path.isfile('./financedata/kospi/' + items["Name"] + '.html') :
            bs = GetBalanceSheet(items["Code"])
            if bs is not None :
                finance = MakeDataFrame(bs)
                finance.to_html('./financedata/kospi/html/' + items["Name"] + '.html')
                finance.to_csv('./financedata/kospi/csv/' + items["Name"] + '.csv', mode = 'w')
                print(tabulate(finance, headers='keys', tablefmt='psql'))

GetAllBalanceData()