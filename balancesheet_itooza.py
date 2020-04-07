import requests
from bs4 import BeautifulSoup
from bs4 import BeautifulSoup
from requests import get
import numpy as np
import pandas as pd
from tabulate import tabulate
from companycode import stock_code
from get_balancesheet import *
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
    return int(now_price.replace(',', ''))

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
    try : return geometric_mean(roes) - 100
    except : return 0

def GetEPS(finance, num = 1, type = 'run') :
    EPS = finance.iloc[0]   # Get ROE value 
    if type == 'debug' : 
        print(f'EPS datas are {EPS}')
    EPS = [value for value in EPS if not ((value == "N/A") or (value == '0'))]
    EPSs = [value for value in EPS][0:(lambda x: len(EPS) if x == 0 else x)(num)]
    if type == 'debug' :
        print(f'EPSs datas are {EPSs}')
    try : return int(EPS[0].replace(',', ''))
    except : return 0.001

def GetBPS(finance, num = 1, type = 'run') :
    BPS = finance.iloc[3]   # Get ROE value 
    if type == 'debug' : 
        print(f'BPS datas are {BPS}')
    BPS = [value for value in BPS if value != "N/A"]
    BPSs = [value for value in BPS][0:(lambda x: len(BPS) if x == 0 else x)(num)]
    if type == 'debug' :
        print(f'BPSs datas are {BPSs}')
    try : return int(BPS[0].replace(',', ''))
    except : return 0

def GetAllo(finance, num = 1, type = 'run') :
    ALLO = finance.iloc[6]   # Get ROE value 
    if type == 'debug' : 
        print(f'ALLO datas are {ALLO}')
    ALLO = [value for value in ALLO if value != "N/A"]
    AllOs = [value for value in ALLO][0:(lambda x: len(ALLO) if x == 0 else x)(num)]
    if type == 'debug' :
        print(f'AllOs datas are {AllOs}')
    try : return float(AllOs[0])
    except : return 0

def MakeDataStorage(company) :
    Storage = {}
    # Storage['code'] = company
    Storage['code'] = stock_code.iloc[stock_code.index[stock_code['Name'] == company]]['Code'].iloc[0]
    #Storage['name'] = stock_code.iloc[stock_code.index[stock_code['Code'] == company]]['Name'].iloc[0]
    Storage['name'] = company
    company_code = Storage['code']
    # print(Storage['code'])
    try : Storage['bs_Annualized'] = GetDataFrame(company_code, 'Annualized')
    except : Storage['bs_Annualized'] = None
    # print(f"{Storage['bs_Annualized']}")
    try : Storage['bs_Year'] = GetDataFrame(company_code, 'Year')
    except : Storage['bs_Year'] = None

    if(Storage['bs_Annualized'] is None) :
        print(f"Failing   ... {Storage['name']} BalanceSheet can't be crolled")
        return None
    if(Storage['bs_Year'] is None) :
        print(f"Failing   ... {Storage['name']} BalanceSheet can't be crolled")
        return None

    if(Storage['code'] is not None) :
        Storage['value'] = get_price(company_code)
           
        Storage['ROE10'] = GetGeoMeanROE(Storage['bs_Year'])         # 10 years roe geomean
        Storage['ROE5'] = GetGeoMeanROE(Storage['bs_Year'], 5)       # 5 years roe geomean
        Storage['ROE3'] = GetGeoMeanROE(Storage['bs_Annualized'])    # 3 years roe geomean
        Storage['ROEy'] = GetGeoMeanROE(Storage['bs_Annualized'], 4) # 1 years roe geomean 
        Storage['ROEq'] = GetGeoMeanROE(Storage['bs_Annualized'], 1) # 1 quarter roe geomean
        Storage['EPSq'] = GetEPS(Storage['bs_Annualized'], 1) # 1 quarter roe geomean
        Storage['BPSq'] = GetBPS(Storage['bs_Annualized'], 1) # 1 quarter roe geomean
        if Storage['BPSq'] < 0 : Storage['BPSq'] = 0.001

        try : Storage['배당'] = GetAllo(Storage['bs_Year'], 1) # 1 quarter roe geomean
        except : Storage['배당'] = 0
        try : Storage['PER'] = Storage['value'] / Storage['EPSq']
        except ZeroDivisionError : Storage['PER'] = 'N/A'
        try : Storage['PBR'] = Storage['value'] / Storage['BPSq'] # 1 quarter roe geomean
        except ZeroDivisionError : Storage['PBR'] = 'N/A'
        Storage['FV10'] = pow((Storage['ROE10']+100)/100, 10) * Storage['BPSq']
        Storage['FV5'] = pow((Storage['ROE5']+100)/100, 10) * Storage['BPSq']
        Storage['FV3'] = pow((Storage['ROE3']+100)/100, 10) * Storage['BPSq']
        Storage['FVy'] = pow((Storage['ROEy']+100)/100, 10) * Storage['BPSq']
        Storage['FVq'] = pow((Storage['ROEq']+100)/100, 10) * Storage['BPSq']
        Storage['EX10'] = (pow(Storage['FV10'] / Storage['value'], 0.1)-1)*100 # 1 quarter roe geomean
        Storage['EX5'] = (pow(Storage['FV5'] / Storage['value'], 0.1)-1)*100 # 1 quarter roe geomean
        Storage['EX3'] = (pow(Storage['FV3'] / Storage['value'], 0.1)-1)*100 # 1 quarter roe geomean
        Storage['EXy'] = (pow(Storage['FVy'] / Storage['value'], 0.1)-1)*100 # 1 quarter roe geomean
        Storage['EXq'] = (pow(Storage['FVq'] / Storage['value'], 0.1)-1)*100 # 1 quarter roe geomean
        # Storage['가격5'] = Storage['미래가치'] / pow(1.05, 10) # 1 quarter roe geomean
        # Storage['이득5'] = Storage['가격5'] / Storage['value'] * 100 # 1 quarter roe geomean
        # Storage['가격10'] = Storage['미래가치'] / pow(1.10, 10) # 1 quarter roe geomean
        # Storage['이득10'] = Storage['가격10'] / Storage['value'] * 100 # 1 quarter roe geomean
        # Storage['가격15'] = Storage['미래가치'] / pow(1.15, 10) # 1 quarter roe geomean
        # Storage['이득15'] = Storage['가격15'] / Storage['value'] * 100 # 1 quarter roe geomean
        # Storage['가격20'] = Storage['미래가치'] / pow(1.20, 10) # 1 quarter roe geomean
        # Storage['이득20'] = Storage['가격20'] / Storage['value'] * 100 # 1 quarter roe geomean
    # print(Storage)
    return Storage
    

# GetImportantData(MakeDataStorage('삼성전자'))
# d = pd.DataFrame(list(MakeDataStorage('삼성전자').items()), columns=['name', 'vaule', 'ROE10', 'ROE5', 'ROE3', 'ROEy', 'ROEq', 'EPSq', \
#     'BPSq', '배당', 'PER', 'PBR', '미래가치', '기대ROE', '가격5', '이득5', '가격10', '이득10', '가격15', '이득15', '가격20', '이득20'])
df = pd.DataFrame()
DataList = []
def MakeDataFrameforDisplay(Data) :
    if Data is not None :
        print(f"Progrssing... {Data['name']}")
        del Data['bs_Annualized']
        del Data['bs_Year']
        # print(f"{Data}")
        DataList.append(Data)
        # print(DataList)





# print(df)
#d = pd.DataFrame(list(MakeDataStorage('삼성전자').items()), columns=['name'])
# print(d)
# DBlist.append(MakeDataStorage('SK하이닉스'))
# DBlist.append(MakeDataStorage('카카오'))
# DBlist.append(MakeDataStorage('한양이엔지'))    
# DBlist.append(MakeDataStorage('프로텍'))
# DBlist.append(MakeDataStorage('월덱스'))
# DBlist.append(MakeDataStorage('한국알콜'))
# DBlist.append(MakeDataStorage('아세아제지'))

# print(DBlist)
# for datas in DBlist :
#     print(f" {datas['name']}'s ROE3 is {datas['ROE3']}")

#finance = MakeDataFrame(GetBalanceSheet("005930"))

# print(tabulate(finance, headers='keys', tablefmt='psql'))
# print(finance.describe())


# ROE_y = finance.iloc[7]   # Get ROE value 

# for data in ROE_y :
#    print(type(data), data)

# print([float(value) for value in ROE_y])
# print(type(ROE_y), ROE_y, geometric_mean([float(value) for value in ROE_y]))
# finance.to_html('./financedata/finance.html')
# print(tabulate(finance, headers='keys', tablefmt='psql'))

