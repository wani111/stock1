import pandas as pd

allstocklist_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13', header=0)[0]
kospilist_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13&marketType=stockMkt', header=0)[0]
kosdaqlist_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13&marketType=kosdaqMkt', header=0)[0]
konexlist_df = pd.read_html('http://kind.krx.co.kr/corpgeneral/corpList.do?method=download&searchType=13&marketType=konexMkt', header=0)[0]

# kospilist_db = pd.DataFrame(kospilist_df)
# kosdaqlist_db = pd.DataFrame(kosdaqlist_df)
# konexlist_db = pd.DataFrame(konexlist_df)

allstocklist_df = allstocklist_df.rename(columns={"회사명": "Name", "종목코드": "Code"}, errors="raise")
# kospilist_df = kospilist_df.rename(columns={"회사명": "Name", "종목코드": "Code"}, errors="raise")
# kosdaqlist_df = kosdaqlist_df.rename(columns={"회사명": "Name", "종목코드": "Code"}, errors="raise")
# konexlist_df = konexlist_df.rename(columns={"회사명": "Name", "종목코드": "Code"}, errors="raise")

print(allstocklist_df[['Name', 'Code']])
# print(kospilist_df[['Name', 'Code']])
# print(kosdaqlist_df[['Name', 'Code']])
# print(konexlist_df[['Name', 'Code']])
