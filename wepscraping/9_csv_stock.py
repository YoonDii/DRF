#액셀파일로 저장하는 연습

import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

for page in range(1,5): # 4페이지까지 돌기
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    date_rows = soup.find("table", attrs = {"class":"type_2"}).find("tbody").find_all()
    for row in date_rows:
        colums = row.find_all("td")
        if len(colums) <= 1 : #의미없는 데이터는 skip
            continue
        date = [colum.get_text() for colum in colums]
        print(date)