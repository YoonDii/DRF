from datetime import datetime

# 인풋을 아웃풋으로 변환하여 출력하라  인풋은 날짜,문자열 등 다양/ 아웃풋은 2023-02-01 00:00:00 이렇게 나와야함

# Q1
date1 = datetime(
    2023,
    2,
    1,
    0,
    0,
    0,
)
print(date1)  # 2023-02-01 00:00:00

# Q2
date2 = datetime.now()
print(date2.strftime("%Y-%m-%d %04:%00:%00"))
# 2023-02-02 4:0:0


# Q3
input = "김은정은 2023년 02월 01일 입력을 하였다."
ans = input.split()
print(ans)  # ['김은정은', '2023년', '02월', '01일', '입력을', '하였다.']
print(ans[1], ans[2], ans[3])  # 2023년 02월 01일
print(ans[1] + ans[2] + ans[3])  # 2023년02월01일
result = ans[1] + ans[2] + ans[3]
print(result, type(result))  # 2023년02월01일 <class 'str'>
date3_format = "%Y년%m월%d일"
date3 = datetime.strptime(result, date3_format)
print(date3)  # 2023-02-01 00:00:00
