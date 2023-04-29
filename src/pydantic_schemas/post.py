from pydantic import BaseModel, validator

class Post(BaseModel):
    id: int
    # title: str
    @validator('id')
    def check_that_id_less_then_two(cls, v):
        if v < 0:
            raise ValueError('id is less then null')
        else:
            return v
