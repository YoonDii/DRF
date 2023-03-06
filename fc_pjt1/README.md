# 미니실습1
## 뉴스기사 3줄요약하기

  1. 바이너리 파일을 문자열로 변경하자
  `import base64`를 사용해서 사용가능!
  이미지 가져오기 등 가능!

  2. 문자열을 원하는대로 추출하자
  `import txtwrap`
  `import re` 정규표현식
  둘 다 많은 함수들이 있으니 꼭 공식문서 확인하기!

  3. 단어 개수를 구하자
  `collections.Counter`를 사용하면 된다.
  `import collection`한 다음 원하는 단어의 개수 찾아주면 됨.
  `collections.Counter(인스턴스)`

  4. 문서를 요약하자 
  gensim : 자연어 처리, 토픽 모델링에 사용되는 파이썬 머신러닝 라이브러리
  `pip install gensim==3.7.3` 
  4.x인 최신버전은 summarization내장모듈이 지원이 안되기 때문에 그 밑의 버전으로 깔아야한다.

  5. 텍스트 파일 저장
  `파일객체 = open(파일 이름,파일 열기 모드)`
  `파일 객체.close()`

  6. 실습하기
  