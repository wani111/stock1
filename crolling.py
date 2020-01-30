import requests
from bs4 import BeautifulSoup
from companycode import stock_code
import numpy as np
import pandas as pd

# company_code를 입력받아 bs_obj를 출력
def get_bs_obj(company_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    result = requests.get(url)
    bs_obj = BeautifulSoup(result.content, "html.parser")
    return bs_obj

def get_balance_obj(company_code):
    url = "https://finance.naver.com/item/main.nhn?code=" + company_code
    result = requests.get(url)
    balance_obj = BeautifulSoup(result.content, "html.parser")
    
    finance_html = balance_obj.select('div.section.cop_analysis div.sub_section')[0]

    # with open('crollingdata.html', 'w') as crollingdata:
	#     print(balance_obj, file=crollingdata)

    th_data = [item.get_text().strip() for item in finance_html.select('thead th')]
    annual_date = th_data[3:7]
    quarter_date = th_data[7:13]

    finance_index = [item.get_text().strip() for item in finance_html.select('th.h_th2')][3:]
    finance_data = [item.get_text().strip() for item in finance_html.select('td')]

    # print(annual_date)
    # print(quarter_date)
    # print(finance_index)
    

    finance_data = np.array(finance_data)
    finance_data.resize(len(finance_index), 10)

    #print(finance_data)
    
    finance_date = annual_date + quarter_date
    finance = pd.DataFrame(data=finance_data[0:,0:], index=finance_index, columns=finance_date)
    annual_finance = finance.iloc[:, :4]
    quarter_finance = finance.iloc[:, 4:]

    # print(annual_finance)
    # print(quarter_finance)

    #print(quarter_finance)
    #print("-------------------------------")

    Roe_list =[] 
  
    # # Iterate over each row 
    # for index, cols in quarter_finance.iterrows(): 
    #     # Create list for the current row 
    #     my_list = cols("ROE(지배주주)") 
        
    #     # append the list to the final list 
    #     Row_list.append(my_list) 

    for value in quarter_finance.iloc[5]:
        Roe_list.append(value)

    #print(Roe_list)
    #print(finance_html)
    return Roe_list


# company_code를 입력받아 now_price를 출력
def get_price(company_code):
    #print("get_price " + company_code)
    bs_obj = get_bs_obj(company_code)
    no_today = bs_obj.find("p", {"class": "no_today"})
    blind = no_today.find("span", {"class": "blind"})
    now_price = blind.text
    return now_price
 
def get_roe(company_code):
    #print("get_price " + company_code)
    balance_obj = get_balance_obj(company_code)
    roe_val = balance_obj.find_all("table", {"class": "gHead01 all-width"})
    #print(roe_val.prettify())
    #blind = no_today.find("span", {"class": "blind"})
    #now_price = blind.text
    return roe_val


# 펄어비스 회사 코드는 ”263750”
# 삼성전자 회사 코드는 ”005930”
# 셀트리온 회사 코드는 ”068270”
company_codes = ["263750", "005930", "068270"]

"""
for code in company_codes:
    #now_price = get_price(str(code["종목코드"]))
    print(type(code))
    now_price = get_price(code)
    print(now_price)
"""

print('{0:<20}, {1}, {2}, {3}'.format("Name",  "종목코드", "현재가격", "ROEs"))
for idx, items in stock_code.iterrows():
    now_price = get_price(items["Code"])
    roes = get_balance_obj(items["Code"])
    print('{0:<20}, {1}, {2}, {3}'.format(items["Name"],  items["Code"], now_price, roes))

# for idx, items in stock_code.iterrows():
#     now_roe = get_roe(items["Code"])
#     print('{0:<20}, {1}, {2}'.format(items["Name"],  items["Code"], now_roe))
