import requests
from bs4 import BeautifulSoup

url="https://comic.naver.com/webtoon/list?titleId=650305&weekday=sat"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# cartoons = soup.find_all("td",attrs={"class":"title"})
# title = cartoons[0].a.get_text()#3부33화 구천현녀 랑랑4
# link = cartoons[0].a["href"]
# print(title)
# print(link)#/webtoon/detail?titleId=650305&no=369&weekday=sat
# print("https://comic.naver.com" + link)
#https://comic.naver.com/webtoon/detail?titleId=650305&no=369&weekday=sat

#만화제목과 링크가져오기
# for cartoon in cartoons:
#     title = cartoon.a.get_text()
#     link = "https://comic.naver.com" + cartoon.a["href"]
#     print(title,link)
    # 3부33화 구천현녀 랑랑4 https://comic.naver.com/webtoon/detail?titleId=650305&no=369&weekday=sat
    # 3부32화 구천현녀 랑랑3 https://comic.naver.com/webtoon/detail?titleId=650305&no=368&weekday=sat
    # 3부31화 구천현녀 랑랑2 https://comic.naver.com/webtoon/detail?titleId=650305&no=367&weekday=sat
    # 3부30화 구천현녀 랑랑1 https://comic.naver.com/webtoon/detail?titleId=650305&no=366&weekday=sat
    # 3부29화 전쟁의 여신 https://comic.naver.com/webtoon/detail?titleId=650305&no=365&weekday=sat
    # 3부28화 삼 신(神)의 협공 https://comic.naver.com/webtoon/detail?titleId=650305&no=364&weekday=sat
    # 3부27화 흰산의 영역 밖에서 https://comic.naver.com/webtoon/detail?titleId=650305&no=363&weekday=sat
    # 3부26화 육오의 목숨 https://comic.naver.com/webtoon/detail?titleId=650305&no=362&weekday=sat
    # 3부25화 뇌신(雷神) 풍륭 https://comic.naver.com/webtoon/detail?titleId=650305&no=361&weekday=sat
    # 3부24화 신격(神格)의 등장 https://comic.naver.com/webtoon/detail?titleId=650305&no=360&weekday=sat


#평점구하기
cartoons = soup.find_all("div",attrs={"class":"rating_type"})

total_rates = 0
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    # 9.12
    # 8.96
    # 9.77
    # 9.52
    # 9.83
    # 9.57
    # 9.63
    # 9.73
    # 9.82
    # 9.76

    total_rates += float(rate)
print("전체점수:",total_rates) #전체점수: 95.71
print("평균점수:",total_rates/len(cartoons)) #평균점수: 9.571

#python을 터미널에 입력해서 한줄한줄 확인할수있음!