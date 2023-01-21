import requests
from bs4 import BeautifulSoup

res = requests.get("https://search.daum.net/search?w=tot&q=2022%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR")
res.raise_for_status()

soup = BeautifulSoup(res.text,"lxml")

images = soup.find_all("img",attrs={"class":"thumb_img"})

for idx, image in enumerate(images):
    # print(image["src"])
    image_url = image["src"]
    if image_url.startswith("//"):
        image_url = "https" + image_url
    print(image_url)

    #영화포스터이미지가져오기
    image_res = requests.get(image_url)
    image_res.raise_for_status()

    with open("movie{}.jpg".format(idx+1), "wb") as f:
        f.write(image_res.content)
        #랭킹30위까지 가져와짐 일단 지움

    if idx >= 4: #상위 5개 이미지까지만 다운로드
        break  # 5개 잘 가져와짐

    
