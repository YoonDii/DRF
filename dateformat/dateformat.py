from datetime import datetime


date1 = datetime(
    2023,
    2,
    1,
    0,
    0,
    0,
)
print(date1)  # 2023-02-01 00:00:00

date2 = datetime.now()
print(date2.strftime("%Y-%m-%d %04:%00:%00"))
# 2023-02-02 4:0:0

input = "김은정은 2023년 02월 01일 입력을 하였다."
ans = input.split()

print(ans)  # ['김은정은', '2023년', '02월', '01일', '입력을', '하였다.']
print(ans[1], ans[2], ans[3])  # 2023년 02월 01일


# date3_format = "%Y-%m-%d %H:%M:%S"
# date3 = datetime.strptime(input, date3_format)
# print(date3)
