import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title) <title>네이버 웹툰 &gt; 요일별  웹툰 &gt; 전체웹툰</title>
# print(soup.title.get_text()) 네이버 웹툰 > 요일별  웹툰 > 전체웹툰
# print(soup.a) <span>메인 메뉴로 바로가기</span></a>
# // soup 객체에서 처음 발견되는 a element 출력

# print(soup.a.attrs) {'href': '#menu', 'onclick': "document.getElementById('menu').tabIndex=-1;document.getElementById('menu').focus();return false;"}
# // a element의 속성 정보를 출력

# print(soup.a["href"]) #menu
# // a element의 href 속성'값' 정보를 출력

# print(soup.find("a", attrs={"class": "Nbtn_upload"})) //class="Nbtn_upload"인 a element를 찾아줘
# <a class="Nbtn_upload" href="/mypage/myActivity" onclick="nclk_v2(event,'olk.upload');">웹툰 올리기</a>

# print(soup.find(attrs={"class": "Nbtn_upload"})) //class="Nbtn_upload"인 어떤 element를 찾아줘
# <a class="Nbtn_upload" href="/mypage/myActivity" onclick="nclk_v2(event,'olk.upload');">웹툰 올리기</a>

# print(soup.find ("li", attrs={"rank01"}))
rank1 = soup.find("li", attrs={"rank01"})
# print(rank1.a)
# <a href="/webtoon/detail?titleId=570503&amp;no=429" onclick="nclk_v2(event,'rnk*p.cont','570503','1')" title="연애혁명-424. Matters">연애혁명-424. Matters</a>
# print(rank1.a.get_text()) 연애혁명-424. Matters
# print(rank1.next_sibling.next_sibling) # 다음 엘리먼트로 넘어가 출력
# print(rank1.parent)
rank2 = rank1.find_next_sibling("li")
# print(rank2.a.get_text()) 앞집나리-10화 - 시력 -30은 우주방어
rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text()) 현실퀘스트-64화

rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text()) 앞집나리-10화 - 시력 -30은 우주방어

# 한꺼번에 찾기
print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text = "앞집나리")
print(webtoon)