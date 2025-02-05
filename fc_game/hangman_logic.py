# 단어가 랜덤으로 나오게 하기
import random

f = open("voca.txt", "r", encoding="UTF-8")
raw_data = f.read()
f.close()
data_list = raw_data.split("\n")
data_list = data_list[:-1]

while True:
    r_index = random.randrange(0, len(data_list))
    word = data_list[r_index].replace("\xa0", " ").split(" ")[1]
    if len(word) <= 6:
        break
print(word)
# A가 영어 단어를 1개 생각한다.
word = word.upper()
# print(word)

# 단어의 글자 수만큼 밑줄을 긋는다.
word_show = "_" * len(word)
# print(word_show)
try_num = 0  # 오답횟수
ok_list = []
no_list = []

while True:
    # B가 단어에 포함될 것 같은 알파벳을 하나씩 말한다.
    ans = input().upper()
    # print(ans)

    # 알파벳이 단어에 포함되면 밑줄에 알파벳을 패워 놓고
    # 포함되지 않는다면 사람을 1획 씩 그린다.
    result = word.find(ans)  # find함수는 하나만 알려줌

    # print(result)
    if result == -1:
        print("아닙니다~")
        try_num += 1
        no_list.append(ans)
    else:
        print("오,,어떻게 알았지")
        ok_list.append(ans)

        for i in range(len(word)):
            if word[i] == ans:
                word_show = word_show[:i] + ans + word_show[i + 1 :]
        print(word_show)

    # 사람이 먼저 완성되면 출제자 A가 이긴다.
    if try_num == 7:
        break
    # 단어가 먼저 오나성되면 단어를 맞힌 사람 B가 이긴다.
    if word_show.find("_") == -1:
        break
print("정답은 : " + word)
