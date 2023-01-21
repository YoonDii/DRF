import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 엘리먼트 나올때 까지 기다리게하는것
from selenium.webdriver.support import (
    expected_conditions as EC,
)  # 기다리게하는 조건을 뭘로할지 정의해주는것


def wait_until(xpath_str):  # 시간대기함수
    WebDriverWait(browser, 30).until(
        EC.presence_of_element_located((By.XPATH, xpath_str))
    )


browser = webdriver.Chrome()
url = "https://m-flight.naver.com/"
browser.get(url)
begin_date = browser.find_element(By.XPATH, '//button[text()="가는 날"]')
# //는 html전체에서 button[text()="가는 날"] 이거를 찾겠다라는 뜻.
begin_date.click()

# time.sleep(1)  # 1초대기


wait_until('//b[text() ="27"]')  # 나올때까지 30초 대기
day27 = browser.find_elements(By.XPATH, '//b[text() ="27"]')
day27[0].click()

arrival_date = browser.find_element(By.XPATH, '//button[text()="오는 날"]')
arrival_date.click()

day31 = browser.find_elements(By.XPATH, '//b[text()="31"]')
day31[0].click()

arrival = browser.find_element(By.XPATH, '//b[text()="도착"]')
arrival.click()

domestic = browser.find_element(By.XPATH, '//button[text()="국내"]')
domestic.click()

jeju = browser.find_element(By.XPATH, '//i[contains(text(),"제주국제공항")]')
jeju.click()

search = browser.find_element(By.XPATH, '//span[contains(text(),"항공권 검색")]')
search.click()

elem = WebDriverWait(browser, 30).until(
    EC.presence_of_element_located(
        (By.XPATH, '//div[@class="domestic_Flight__sK0eA result"]')
    )
)
# 30초 동안 기다리기 // 30초 안에가져오면 잘된것, 아니면 에러
print(elem.text())
#'아시아나항공\n1%적립이벤트혜택\n06:05GMP\n07:10CJU\n01시간 05분\n특가석편도 67,300원~\n네이버페이 결제시 1% 적립\n편도 66,627원~'
