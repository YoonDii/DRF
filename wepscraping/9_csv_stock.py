#엑셀파일로 저장하는 연습

import csv
import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename,"w",encoding="utf-8-sig", newline="") #공백을 넣는 이유는 줄바꿈을 없애기위해서
# 엑셀파일에서 한글이 깨진다면 인코딩을 encoding="utf-8-sig" 이렇게 바꾸면 된다.
writer = csv.writer(f)

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
        # print(date)
        writer.writerow(date) #리스트형태로 넣어줘야함