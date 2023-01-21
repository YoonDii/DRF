# chrome;//version 크롬버전확인하기 //108.0.5359.126(이건 노트북)//109.0.5414.87(아이맥)
# cromedriver 검색 후 버전에 맞는 파일 다운로드

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome("./chromedriver.exe")  # 파일있는 경로써주기 같은 곳에 있으면 안써도됨.
browser.get("http://naver.com")

# 터미널에 python입력 후
# >>> from selenium import webdriver
# >>> browser = webdriver.Chrome()
# 입력하면 새로운 창이 나옴
# browser.get("http://naver.com")
# 네이버화면으로 전환
# 이 화면에서도 검사페이지 활용 가능

# elem = browser.find_element(By.CLASS_NAME,"link_login")
# 로그인버튼 엘리먼트를 찾아서 변수로 지정
# elem
# elem.click() 로그인버튼 클릭

# browser.back()  이전버튼
# browser.forward() 다음버튼
# browser.refrash() 새로고침버튼

# from selenium.webdriver.common.keys import Keys
# elem.send_keys(Keys.ENTER)
