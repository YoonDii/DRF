import requests

# res = requests.get("http://naver.com")
res = requests.get("http://google.com")
res.raise_for_status()  # 문제가 없으면 진행하고 문제가 있으면 오류메세지와 함께 멈춘다.두줄은 쌍으로 쓴다.
# res = requests.get("http://yoondii.tistory.com")
# res = requests.get("https://www.wanted.co.kr")
# print("응답코드 :", res.status_code)  # 200이면 정상


# if res.status_code == requests.codes.ok:  # 코드가 200이면 이랑 같은 말
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다.[에러코드", res.status_code, "]")

# res.raise_for_status()
# print("웹 스크래핑을 진행합니다.")

print(len(res.text))  # 네이버184946 #구글 15180 //근데 할때 마다 달라지넹
print(res.text)


with open("mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)  # html파일이 생기고, 열어보면 짭구글 페이지 나옴
