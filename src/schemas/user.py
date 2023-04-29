from pydantic import BaseModel, validator
from src.enums.user_enums import Genders, Statuses, UsersErorrs
class User(BaseModel):
    id: int
    name: str
    email: str
    gender: Genders
    status: Statuses

    @validator('email')
    def check_that_dog_in_email_address(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError(UsersErorrs.WRONG_EMAIL.value)
