import pandas as pd
import numpy as np

allstocklist_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]
kospilist_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13&marketType=stockMkt', header=0)[0]
kosdaqlist_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13&marketType=kosdaqMkt', header=0)[0]
konexlist_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13&marketType=konexMkt', header=0)[0]

# kospilist_db = pd.DataFrame(kospilist_df)
# kosdaqlist_db = pd.DataFrame(kosdaqlist_df)
# konexlist_db = pd.DataFrame(konexlist_df)

allstocklist_df = allstocklist_df.rename(columns={"회사명": "Name", "종목코드": "Code"}, errors="raise")
kospilist_df = kospilist_df.rename(columns={"회사명": "Name", "종목코드": "Code"}, errors="raise")
kosdaqlist_df = kosdaqlist_df.rename(columns={"회사명": "Name", "종목코드": "Code"}, errors="raise")
konexlist_df = konexlist_df.rename(columns={"회사명": "Name", "종목코드": "Code"}, errors="raise")


stock_code = allstocklist_df[['Code', 'Name']]
kospi_stock_code = kospilist_df[['Code', 'Name']]
kosdaq_stock_code = kosdaqlist_df[['Code', 'Name']]
konex_stock_code = konexlist_df[['Code', 'Name']]

stock_code = stock_code.applymap(str)
kospi_stock_code = kospi_stock_code.applymap(str)
kosdaq_stock_code = kosdaq_stock_code.applymap(str)
konex_stock_code = konex_stock_code.applymap(str)

stock_code['Code'] = stock_code['Code'].str.zfill(6)
kospi_stock_code['Code'] = kospi_stock_code['Code'].str.zfill(6)
kosdaq_stock_code['Code'] = kosdaq_stock_code['Code'].str.zfill(6)
konex_stock_code['Code'] = konex_stock_code['Code'].str.zfill(6)

stock_code.sort_values(by='Name', ascending=False)
kospi_stock_code.sort_values(by='Name', ascending=False)
kosdaq_stock_code.sort_values(by='Name', ascending=False)
konex_stock_code.sort_values(by='Name', ascending=False)

# print(type(stock_code['Code'][2]), stock_code['Code'][2])
# print(type(stock_code['Name'][2]), stock_code['Name'][2])
# print(type(kospi_stock_code['Code'][2]), kospi_stock_code['Code'][2])
# print(type(kospi_stock_code['Name'][2]), kospi_stock_code['Name'][2])
# print(type(kosdaq_stock_code['Code'][2]), kosdaq_stock_code['Code'][2])
# print(type(kosdaq_stock_code['Name'][2]), kosdaq_stock_code['Name'][2])
# print(type(konex_stock_code['Code'][2]), konex_stock_code['Code'][2])
# print(type(konex_stock_code['Name'][2]), konex_stock_code['Name'][2])

print(stock_code)


# csv 파일을 해석하여 dataframe으로 변환하고, stock_data 변수에 저장
# stock_data = pd.read_csv("AllStockCode.csv", low_memory=False, dtype=str)
# stock_code = stock_data[["Code", "Name"]]


# kospi_stock_data = pd.read_csv("kospi.csv", low_memory=False, dtype=str)
# kospi_stock_code = kospi_stock_data[["Code", "Name"]]

# kosdaq_stock_data = pd.read_csv("kosdaq.csv", low_memory=False, dtype=str)
# kosdaq_stock_code = kosdaq_stock_data[["Code", "Name"]]

# print(f'{stock_data["Code"].tolist()}  {type(stock_data["Code"].tolist())}')
