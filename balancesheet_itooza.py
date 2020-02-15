import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
from requests import get
import numpy as np
import pandas as pd
from tabulate import tabulate
from companycode import stock_code
import os.path 
from statistics import geometric_mean

def get_bs_obj(company_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

def get_price(company_code):
    #print("get_price " + company_code)
    bs_obj = get_bs_obj(company_code)
    no_today = bs_obj.find("p", {"class": "no_today"})
    blind = no_today.find("span", {"class": "blind"})
    now_price = blind.text
    # print(f'price is {now_price}')
    return now_price

def GetBalanceSheet(company_code, type = 'Annualized'):
    url = "http://search.itooza.com/index.htm?seName=" + company_code
    r = get(url)
    soup = BeautifulSoup(r.content.decode('euc-kr','replace'), 'html.parser')
    if(type == 'Annualized') :
        table = soup.find("div", {"id": "indexTable1"})
    elif(type == 'Year') :
        table = soup.find("div", {"id": "indexTable2"})
    # print(table)
    return table

def MakeDataFrame(bs):
    finance_date = [item.get_text().strip() for item in bs.select('thead th')]
    finance_index = [item.get_text().strip() for item in bs.select('tbody th')]
    # finance_index = ["EPS(연)", "EPS(개)", "PER", "BPS", "PBR", "주배당", "시배당", "ROE", "순이익", "영업이익", "주가"]
    finance_data = [item.get_text().strip() for item in bs.select('tbody td')]
    with open('bstable', 'w', encoding='utf-8') as bstable:
        print(bs, file=bstable)

    finance_data = np.array(finance_data)       # change finance_data to numpy array
    finance_data.resize(len(finance_index), 12) # resize len(finance_index) x 12

    # print(len(finance_date[1:]))
    # print(finance_date[1:])

    # print(len(finance_index))
    # print(finance_index)
    # print(finance_data)


    # my_2darray = np.array([[1, 2, 3], [4, 5, 6]])
    # print(pd.DataFrame(finance_data))
    finance = pd.DataFrame(data=finance_data, index=finance_index, columns=finance_date[1:])
    # annual_finance = finance.iloc[:, :4]
    # quarter_finance = finance.iloc[:, 4:]
    # print(finance_index)
    # print(finance_data)
    return finance

def GetAllBalanceData() :
    for idx, items in stock_code.iterrows():
        if not os.path.isfile('./financedata/kospi/' + items["Name"] + '.html') :
            bs = GetBalanceSheet(items["Code"])
            if bs is not None :
                finance = MakeDataFrame(bs)
                finance.to_html('./financedata/kospi/' + items["Name"] + '.html')
                print(tabulate(finance, headers='keys', tablefmt='psql'))

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def GetGeoMeanROE(finance, num = 0) :
    ROE = finance.iloc[7]   # Get ROE value 
    # print(f'ROE datas are {ROE}')
    # for data in ROE_y :
    #     print(type(data), data)

    # a = (lambda x: len(ROE) if x == 0 else x)(num)
    # print(a)
    ROE = [float(value) + 100 for value in ROE if isfloat(value)]
    roes = [value for value in ROE][0:(lambda x: len(ROE) if x == 0 else x)(num)]
    #print(f'roes datas are {roes}')
    # newroe = []
    # for data in roes:
    #     if isfloat(data) :
    #         newroe.append(float(data) + 100) 

    # print(f'newroe datas are {newroe}')
    # print(type(ROE), ROE, geometric_mean([float(value) for value in ROE]))
    return geometric_mean(roes) - 100


def MakeDataStorage(company) :
    Storage = {}
    
    
    # Storage['code'] = company
    Storage['code'] = stock_code.iloc[stock_code.index[stock_code['Name'] == company]]['Code'].iloc[0]
    
    # Storage['name'] = stock_code.iloc[stock_code.index[stock_code['Code'] == company]]['Name'].iloc[0]
    Storage['name'] = company

    company_code = Storage['code']

    # print(Storage['code'])
    if(Storage['code'] is not None) :
        Storage['value'] = get_price(company_code)
        Storage['bs_Annualized'] = MakeDataFrame(GetBalanceSheet(company_code, 'Annualized'))
        Storage['bs_Year'] = MakeDataFrame(GetBalanceSheet(company_code, 'Year'))
        Storage['ROE10'] = GetGeoMeanROE(Storage['bs_Year'])         # 10 years roe geomean
        Storage['ROE5'] = GetGeoMeanROE(Storage['bs_Year'], 5)       # 5 years roe geomean
        Storage['ROE3'] = GetGeoMeanROE(Storage['bs_Annualized'])    # 3 years roe geomean
        Storage['ROEy'] = GetGeoMeanROE(Storage['bs_Annualized'], 4) # 1 years roe geomean 
        Storage['ROEq'] = GetGeoMeanROE(Storage['bs_Annualized'], 1) # 1 quarter roe geomean
    # print(Storage)
    return Storage
    

DBlist = []
DBlist.append(MakeDataStorage('삼성전자'))
DBlist.append(MakeDataStorage('SK하이닉스'))
DBlist.append(MakeDataStorage('카카오'))
DBlist.append(MakeDataStorage('한양이엔지'))    
DBlist.append(MakeDataStorage('프로텍'))
DBlist.append(MakeDataStorage('월덱스'))
DBlist.append(MakeDataStorage('한국알콜'))
DBlist.append(MakeDataStorage('아세아제지'))

for datas in DBlist :
    print(f" {datas['name']}'s ROE3 is {datas['ROE3']}")

#finance = MakeDataFrame(GetBalanceSheet("005930"))

# print(tabulate(finance, headers='keys', tablefmt='psql'))
# print(finance.describe())

StockIndex = ['종목명', '현재가', 'ROE(10)', 'ROE(5)', 'ROE(Y)', 'ROE(Q)']




# ROE_y = finance.iloc[7]   # Get ROE value 

# for data in ROE_y :
#    print(type(data), data)

# print([float(value) for value in ROE_y])
# print(type(ROE_y), ROE_y, geometric_mean([float(value) for value in ROE_y]))
# finance.to_html('./financedata/finance.html')
# print(tabulate(finance, headers='keys', tablefmt='psql'))

