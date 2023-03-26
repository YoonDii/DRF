import contextlib
#데이터베이스연결하는 역할
from sqlalchemy import create_engine 
#orm정의하는 역할
from sqlalchemy.ext.declarative import declarative_base 
#session객체를 생성하는 팩토리함수, session객체는 데이터베이스와 상호작용하기위한 인터페이스 역할
from sqlalchemy.orm import sessionmaker 


SQLALCHEMY_DATABASE_URL = "sqlite:///./jumpto_fastapi.db"
# create_engine은 컨넥션 풀을 생성한다. 
# 컨넥션 풀이란 데이터베이스에 접속하는 객체를 일정 갯수만큼 만들어 놓고 돌려가며 사용하는 것을 말한다. 
# (컨넥션 풀은 데이터 베이스에 접속하는 세션수를 제어하고, 또 세션 접속에 소요되는 시간을 줄이고자 하는 용도로 사용한다.)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread':False}
)
SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base = declarative_base()

@contextlib.contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        