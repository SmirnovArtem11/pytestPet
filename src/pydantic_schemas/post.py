from pydantic import BaseModel, validator

class Post(BaseModel):
    id: int
    title: str
    @validator('id')
    def check_that_id_less_then_two(cls, v):
        if v > 2:
            raise ValueError('id is not less then two')
        else:
            return v
