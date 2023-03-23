# pip install fastapi 먼저 설치하기!
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"index": "FastAPI 안녕"}


@app.get("/math/sum")
def math_sum(number_1: int, number_2: int):
    return {"reuslt": number_1 + number_2}


@app.get("/math/mul")
def math_mul(number_1: int, number_2: int = 3):  # number_2는 defult값으로 3을 지정
    return {"result": number_1 * number_2}
