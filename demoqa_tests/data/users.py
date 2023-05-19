import dataclasses
from typing import List
from datetime import date


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    birthday: date
    subjects: List[str]
    hobby: str
    hobbies: str
    picture: str
    address: str
    state: str
    city: str

