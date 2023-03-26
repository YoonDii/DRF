from fastapi import APIRouter

# from database import SessionLocal
from database import get_db
from models import Question

router = APIRouter(
    prefix="/api/question",
)
# #라우팅이란 FastAPI가 요청받은 URL을 해석하여 그에 맞는 함수를 실행하여 그 결과를 리턴하는 행위
# @router.get("/list")
# def question_list():
#     db = SessionLocal()
#     _question_list = db.query(Question).order_by(Question.creates.desc()).all()
#     db.close() # 사용한 세션을 컨넥션 풀에 반환하는 함수
#     return _question_list

@router.get("/list")
def question_list():
    with get_db() as db :
        _question_list = db.query(Question).order_by(Question.creates.desc()).all()
        return _question_list