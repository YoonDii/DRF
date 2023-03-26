import datetime

from pydantic import BaseModel

class Question(BaseModel):
    id : int
    subject : str
    content : str
    create_date: datetime.datetime
    #4가지 항목 모두 디폴트값이 없기때문에 필수항목이다.

    class Config:
        orm_mode = True