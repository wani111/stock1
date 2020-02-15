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
    return int(now_price.replace(',', ''))

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
    # with open('bstable', 'w', encoding='utf-8') as bstable:
    #     print(bs, file=bstable)

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
    # print(finance)
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

def GetEPS(finance, num = 1, type = 'run') :
    EPS = finance.iloc[0]   # Get ROE value 
    if type == 'debug' : 
        print(f'EPS datas are {EPS}')
    EPS = [value for value in EPS if not ((value == "N/A") or (value == '0'))]
    EPSs = [value for value in EPS][0:(lambda x: len(EPS) if x == 0 else x)(num)]
    if type == 'debug' :
        print(f'EPSs datas are {EPSs}')
    return int(EPS[0].replace(',', ''))

def GetBPS(finance, num = 1, type = 'run') :
    BPS = finance.iloc[3]   # Get ROE value 
    if type == 'debug' : 
        print(f'BPS datas are {BPS}')
    BPS = [value for value in BPS if value != "N/A"]
    BPSs = [value for value in BPS][0:(lambda x: len(BPS) if x == 0 else x)(num)]
    if type == 'debug' :
        print(f'BPSs datas are {BPSs}')
    return int(BPS[0].replace(',', ''))

def GetAllo(finance, num = 1, type = 'run') :
    ALLO = finance.iloc[6]   # Get ROE value 
    if type == 'debug' : 
        print(f'ALLO datas are {ALLO}')
    ALLO = [value for value in ALLO if value != "N/A"]
    AllOs = [value for value in ALLO][0:(lambda x: len(ALLO) if x == 0 else x)(num)]
    if type == 'debug' :
        print(f'AllOs datas are {AllOs}')
    return float(AllOs[0])


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
        # print(f"{Storage['bs_Annualized']}")
        Storage['bs_Year'] = MakeDataFrame(GetBalanceSheet(company_code, 'Year'))
        Storage['ROE10'] = GetGeoMeanROE(Storage['bs_Year'])         # 10 years roe geomean
        Storage['ROE5'] = GetGeoMeanROE(Storage['bs_Year'], 5)       # 5 years roe geomean
        Storage['ROE3'] = GetGeoMeanROE(Storage['bs_Annualized'])    # 3 years roe geomean
        Storage['ROEy'] = GetGeoMeanROE(Storage['bs_Annualized'], 4) # 1 years roe geomean 
        Storage['ROEq'] = GetGeoMeanROE(Storage['bs_Annualized'], 1) # 1 quarter roe geomean
        Storage['EPSq'] = GetEPS(Storage['bs_Annualized'], 1) # 1 quarter roe geomean
        Storage['BPSq'] = GetBPS(Storage['bs_Annualized'], 1) # 1 quarter roe geomean
        Storage['배당'] = GetAllo(Storage['bs_Year'], 1) # 1 quarter roe geomean
        try : Storage['PER'] = Storage['value'] / Storage['EPSq']
        except ZeroDivisionError : Storage['PER'] = 'infinite'
        Storage['PBR'] = Storage['value'] / Storage['BPSq'] # 1 quarter roe geomean
        Storage['미래가치'] = pow((Storage['ROE3']+100)/100, 10) * Storage['BPSq']
        Storage['기대ROE'] = (pow(Storage['미래가치'] / Storage['value'], 0.1)-1)*100 # 1 quarter roe geomean
        Storage['가격5'] = Storage['미래가치'] / pow(1.05, 10) # 1 quarter roe geomean
        Storage['이득5'] = Storage['가격5'] / Storage['value'] * 100 # 1 quarter roe geomean
        Storage['가격10'] = Storage['미래가치'] / pow(1.10, 10) # 1 quarter roe geomean
        Storage['이득10'] = Storage['가격10'] / Storage['value'] * 100 # 1 quarter roe geomean
        Storage['가격15'] = Storage['미래가치'] / pow(1.15, 10) # 1 quarter roe geomean
        Storage['이득15'] = Storage['가격15'] / Storage['value'] * 100 # 1 quarter roe geomean
        Storage['가격20'] = Storage['미래가치'] / pow(1.20, 10) # 1 quarter roe geomean
        Storage['이득20'] = Storage['가격20'] / Storage['value'] * 100 # 1 quarter roe geomean
    # print(Storage)
    return Storage
    

# GetImportantData(MakeDataStorage('삼성전자'))
# d = pd.DataFrame(list(MakeDataStorage('삼성전자').items()), columns=['name', 'vaule', 'ROE10', 'ROE5', 'ROE3', 'ROEy', 'ROEq', 'EPSq', \
#     'BPSq', '배당', 'PER', 'PBR', '미래가치', '기대ROE', '가격5', '이득5', '가격10', '이득10', '가격15', '이득15', '가격20', '이득20'])
df = pd.DataFrame()
DataList = []
def MakeDataFrameforDisplay(Data) :
    print(f"Progrssing {Data['name']:>10} ......")
    del Data['bs_Annualized']
    del Data['bs_Year']
    DataList.append(Data)
    # print(DataList)


MakeDataFrameforDisplay(MakeDataStorage('삼성전자'))
MakeDataFrameforDisplay(MakeDataStorage('SK하이닉스'))
MakeDataFrameforDisplay(MakeDataStorage('카카오'))
MakeDataFrameforDisplay(MakeDataStorage('한양이엔지'))
MakeDataFrameforDisplay(MakeDataStorage('프로텍'))
MakeDataFrameforDisplay(MakeDataStorage('월덱스'))
MakeDataFrameforDisplay(MakeDataStorage('한국알콜'))
MakeDataFrameforDisplay(MakeDataStorage('아세아제지'))

df = pd.DataFrame(DataList)
df.to_html('./financedata/my.html')
writer = pd.ExcelWriter('stock.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='my')
writer.save()

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

StockIndex = ['종목명', '현재가', 'ROE(10)', 'ROE(5)', 'ROE(Y)', 'ROE(Q)']




# ROE_y = finance.iloc[7]   # Get ROE value 

# for data in ROE_y :
#    print(type(data), data)

# print([float(value) for value in ROE_y])
# print(type(ROE_y), ROE_y, geometric_mean([float(value) for value in ROE_y]))
# finance.to_html('./financedata/finance.html')
# print(tabulate(finance, headers='keys', tablefmt='psql'))

