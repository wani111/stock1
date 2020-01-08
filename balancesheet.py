import requests
from bs4 import BeautifulSoup

URL = "https://finance.naver.com/item/main.nhn?code=005930"

samsung_electronic = requests.get(URL)
html = samsung_electronic.text

soup = BeautifulSoup(html, 'html.parser')

finance_html = soup.select('div.section.cop_analysis div.sub_section')

print(finance_html)
