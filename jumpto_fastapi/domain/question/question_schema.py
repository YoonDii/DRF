import datetime

from pydantic import BaseModel

from domain.answer.answer_schema import Answer

class Question(BaseModel):
    id : int
    subject : str
    content : str
    creates: datetime.datetime
    answers : list[Answer] = []
    #4가지 항목 모두 디폴트값이 없기때문에 필수항목이다.

    class Config:
        orm_mode = True