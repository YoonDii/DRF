from fastapi import FastAPI

from domain.question import question_router
from domain.answer import answer_router

app = FastAPI()

# @app.get("/Hello")
# def hello():
#     return {"message": "안녕하세요 주말입니다"}

app.include_router(question_router.router)
app.include_router(answer_router.router)