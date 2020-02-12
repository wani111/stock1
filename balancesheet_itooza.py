import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
from requests import get
import numpy as np
import pandas as pd
from tabulate import tabulate

def GetBalanceSheet(company_code):
    url = "http://search.itooza.com/index.htm?seName=" + company_code
    r = get(url)
    soup = BeautifulSoup(r.content.decode('euc-kr','replace'), 'html.parser')
    table = soup.find("div", {"id": "indexTable1"})
    # print(table)
    return table
# URL = "https://finance.naver.com/item/main.nhn?code=005930"
# URL = "http://search.itooza.com/index.htm?seName=005930"
# r = requests.get(URL)
# html = r.text

# soup = BeautifulSoup(r.content.decode('euc-kr','replace'), 'html.parser')
# table1 = soup.find("div", {"id": "indexTable3"})
# finance_html = soup.select('div.indexTable1')

# print(table1)
# test()

bs = GetBalanceSheet("005670")
finance_date = [item.get_text().strip() for item in bs.select('thead th')]
# finance_index = [item.get_text().strip() for item in bs.select('th.h_th2')][3:]
finance_index = [item.get_text().strip() for item in bs.select('tbody th')]
finance_data = [item.get_text().strip() for item in bs.select('tbody td')]
with open('bstable', 'w', encoding='utf-8') as bstable:
    print(bs, file=bstable)

finance_data = np.array(finance_data)       # change finance_data to numpy array
finance_data.resize(len(finance_index), 12) # resize len(finance_index) x 12

print(len(finance_date[1:]))
print(finance_date[1:])

print(len(finance_index))
print(finance_index)
# print(finance_data)


# my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
print(pd.DataFrame(finance_data))
finance = pd.DataFrame(data=finance_data, index=finance_index, columns=finance_date[1:])
    # annual_finance = finance.iloc[:, :4]
    # quarter_finance = finance.iloc[:, 4:]

# print(finance_index)
# print(finance_data)
finance.to_html('./financedata/finance.html')
print(tabulate(finance, headers='keys', tablefmt='psql'))