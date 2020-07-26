import pandas as pd

# csv 파일을 해석하여 dataframe으로 변환하고, stock_data 변수에 저장
stock_data = pd.read_csv("AllStockCode.csv", low_memory=False, dtype=str)
stock_code = stock_data[["Code", "Name"]]


kospi_stock_data = pd.read_csv("kospi.csv", low_memory=False, dtype=str)
kospi_stock_code = kospi_stock_data[["Code", "Name"]]

kosdaq_stock_data = pd.read_csv("kosdaq.csv", low_memory=False, dtype=str)
kosdaq_stock_code = kosdaq_stock_data[["Code", "Name"]]

# print(f'{stock_data["Code"].tolist()}  {type(stock_data["Code"].tolist())}')
