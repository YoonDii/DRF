### 이미지를 저장해 주고 서빙하는 API서버

1. imgbb 와 같은 서비스
2. 이미지를 대신 저장
3. Global CDN 서비스
4. 이미지 조회, 삭제, 저장 기능
5. PNG,JPG 등을 webp로 변환

### FastAPI
Annotation Based API Server
1. 비교적 최즉에 등장한 웹프레임워크
2. Python 3.6+부터 지원 (Type Annotation)
3. 내부에서 Starlette과 Pydantic을 사용
4. 풍부한 자유도
5. 자동 스웨거 지원
6. 큰 커뮤니티
7. 아직은 작은 생태계


### 가상환경 설정 후 가상환경 켜고 pip install fastapi 'uvicorn[standard]'설치
### 실행할때는 터미널에 uvicorn main:app --reload 입력
main : 모듈명을 의미합니다. # (main.py)
app : FastAPI로부터 생성된 인스턴스를 의미합니다. # app=FastAPI()
--reload : 코드 수정시 새로고침됨을 의미합니다.