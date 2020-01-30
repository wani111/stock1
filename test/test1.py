from pandas import DataFrame

data = [
    ["037730", "3R", 1510, 7.36],
    ["036360", "3SOFT", 1790, 1.65],
    ["005760", "ACTS", 1185, 1.28],
]
columns = ["종목코드", "종목명", "현재가", "등락률"]
df = DataFrame(data=data, columns=columns)
df = df.set_index("종목코드")
print(df)
#print(df.iloc[0])
#print(df.loc["037730"])