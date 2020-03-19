from balancesheet_itooza import *
from companycode import *
import pandas as pd
import os.path 
from time_folder import pathfolder

def GetAllBalanceData() :
    for idx, items in stock_code.iterrows():
        if not os.path.isfile('./financedata/kospi/Annualized/csv/' + items["Name"] + '.csv') :
            bs = GetBalanceSheet(items["Code"])
            if bs is not None :
                print(f" Annualized {items['Name']}")
                finance = MakeDataFrame(bs)
                finance.to_html('./financedata/kospi/Annualized/html/' + items["Name"] + '.html')
                finance.to_csv('./financedata/kospi/Annualized/csv/' + items["Name"] + '.csv', encoding='utf-8-sig')
        
        if not os.path.isfile('./financedata/kospi/Year/csv/' + items["Name"] + '.csv') :    
            bs = GetBalanceSheet(items["Code"], 'Year')
            if bs is not None :    
                print(f" Year       {items['Name']}")
                finance = MakeDataFrame(bs)
                finance.to_html('./financedata/kospi/Year/html/' + items["Name"] + '.html')
                finance.to_csv('./financedata/kospi/Year/csv/' + items["Name"] + '.csv', encoding='utf-8-sig')
                # print(tabulate(finance, headers='keys', tablefmt='psql'))

# GetAllBalanceData()

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
    # print(finance_date)
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

def GetBalanceSheetFromCSV(company, type = 'Annualized') :
    stock_name = stock_code.iloc[stock_code.index[stock_code['Code'] == company]]['Name'].iloc[0]
    if(type == 'Annualized') :
        df = pd.read_csv('./financedata/kospi/Annualized/csv/' + stock_name + '.csv', index_col = 0, na_filter = False)
    elif(type == 'Year') :
        df = pd.read_csv('./financedata/kospi/Year/csv/' + stock_name + '.csv', index_col = 0, na_filter = False)
    else :
        print('GetBalanceSheetFromCSV Type is not correct')
    
    return df

def GetDataFrame(company, type = 'Annualized') :
    stock_name = stock_code.iloc[stock_code.index[stock_code['Code'] == company]]['Name'].iloc[0]
    
    if(type == 'Annualized') :
        if True : #not os.path.isfile('./financedata/kospi/Annualized/csv/' + stock_name + '.csv') :
            bs = GetBalanceSheet(company, 'Annualized')
            if bs is not None :
                print(f" Annualized {stock_name} data are crolled from Naver..")
                finance = MakeDataFrame(bs)
                finance.to_html('./financedata/kospi/Annualized/html/' + stock_name + '.html')
                finance.to_csv('./financedata/kospi/Annualized/csv/' + stock_name + '.csv', encoding='utf-8-sig')
        else :
            print(f" Annualized {stock_name} data are from CSV..")
            finance = GetBalanceSheetFromCSV(company, 'Annualized')
            
    elif(type == 'Year') :
        if True : #not os.path.isfile('./financedata/kospi/Year/csv/' + stock_name + '.csv') :    
            bs = GetBalanceSheet(company, 'Year')
            if bs is not None :    
                print(f" Year {stock_name} data are crolled from Naver..")
                finance = MakeDataFrame(bs)
                finance.to_html('./financedata/kospi/Year/html/' + stock_name + '.html')
                finance.to_csv('./financedata/kospi/Year/csv/' + stock_name + '.csv', encoding='utf-8-sig')
                # print(tabulate(finance, headers='keys', tablefmt='psql'))
        else :
            print(f" Year {stock_name} data are from CSV..")
            finance = GetBalanceSheetFromCSV(company, 'Year')
    else :
        finance = None
        print('GetDataFrame Type is not correct')
    return finance

Storage = {}
# Storage['fromCrolling'] = MakeDataFrame(GetBalanceSheet('060310', 'Annualized'))
# Storage['fromCSV'] = GetBalanceSheetFromCSV('060310')

# print(f" from Crolling {Storage['fromCrolling']}")

# print(f" from CSV      {Storage['fromCSV']}")

# if Storage['fromCrolling'].equals(Storage['fromCSV']) :
#     print("SAME")
# else :
#     print("not same")
#Storage ['GetData'] = GetDataFrame('003580')