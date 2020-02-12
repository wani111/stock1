# 판다스 모듈 불러오기 (편의 상, pd라는 이름으로 사용)
import pandas as pd

 

# csv 파일을 해석하여 dataframe으로 변환하고, stock_data 변수에 저장
stock_data = pd.read_csv("companycode_copy_2.csv", low_memory=False, dtype=str)

 

#종목코드 컬럼만 선택하여 stock_code 변수에 저장
stock_code = stock_data[["Code", "Name"]]

#print(stock_code)