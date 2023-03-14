import random

f = open("voca.txt", "r", encoding="UTF-8")
raw_data = f.read()
f.close()

# 줄단위로 끊어서 나타내기
print(raw_data.split("\n"))
# 마지막줄 공백제거
data_list = raw_data.split("\n")
data_list = data_list[:-1]

# 리스트안에 /xa0제거하기
data_list[-1].replace("\xa0", " ").split(" ")

while True:
    r_index = random.randrange(0, len(data_list))
    word = data_list[r_index].replace("\xa0", " ").split(" ")[1]
    if len(word) <= 6:  # 6글자가 넘지 않는 단어
        break
    print(word)
