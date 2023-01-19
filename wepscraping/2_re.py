"""
#정규식표현

주민등록번호
990909-1111111

이메일
gratebeckend@google.com

차량번호
11 가 1234
123 가 1234

IP
192.168.0.1
1000.2000.3000.4000
"""
# 정규식라이브러리
import re

# abcd ,book, desk
# cafe, care, case, cave ...
p = re.compile("ca.e")
# . : 하나의 문자를 의미 (ca.e) > cafe, care, case (o) | caffe(x)
# ^ : 문자열의 시작 (^de) > desk, destination (o) | fade(x)
# $ : 문자열의 끝 (se$) > case,base(o) | face (x)


def print_match(m):

    if m:
        print(m.group())
    else:
        print("매칭되지 않음")


m = p.match("case")  # match : 주어진 문자열의 처음부터 일치하는지 확인
print_match(m)
# print(m.group())  # 위에 정규식과 매치가 되어서 출력됨./매치되지 않으면 에러가 발생
