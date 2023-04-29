from enum import Enum

class Genders(Enum):
    female = 'female'
    male = 'male'

class Statuses(Enum):
    inactive ='inactive'
    active ='active'
class UsersErorrs(Enum):
    WRONG_EMAIL ="Email doesn't contain @"