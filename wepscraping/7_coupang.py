import requests
import re
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?component=&q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}
res = requests.get(url,headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")
# print(res.text)

items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
# print(items[0].find("div", attrs={"class":"name"}).get_text())

for item in items:
    ad = item.find("span",attrs = {"class": "ad-badge-text"})
    if ad :
        print("<광고상품은 제외합니다.>")
        continue
    
    name = item.find("div", attrs={"class":"name"}).get_text()#이름
    price =item.find("strong", attrs={"class":"price-value"}).get_text()#제품명
    
    rate = item.find("em",attrs={"class":"rating"})#평점
    #평점없는 제품이 있을 수 있어서 조건문추가
    if rate:
        rate = rate.get_text()
    else:
        rate = "평점없음"
    
    rate_count = item.find("span",attrs={"class":"rating-total-count"})#평점수
    if rate_count:
        rate_count = rate.get_text()
    else:
        rate_count = "평점수 없음"

    print(name,price,rate,rate_count)
    