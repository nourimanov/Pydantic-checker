import json
import string
from pydantic import (
    BaseModel, field_validator,
    model_validator
)

'''
Opened a file called users.json to test using the project!
'''
                                            

class User(BaseModel):
    username: str
    password: str
    age: int
    phone: str


    @field_validator('username')
    @classmethod
    def validate_username(cls, value):
        if any(p in value for p in string.punctuation):     # punctuation: r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
            raise ValueError("User must not include punctuation")
        else:
            return value


    @field_validator('password')
    @classmethod
    def validate_password(cls, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long")
        if any(p in value for p in string.punctuation):     # punctuation: r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
            if any(d in value for d in string.digits):      # digits: 0123456789
                if any(l in value for l in string.ascii_lowercase):    # ascii_lowercase: 'abcdefghijklmnopqrstuvwxyz'
                    if any(u in value for u in string.ascii_uppercase):  # ascii_uppercase: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                        return value
        raise ValueError("Username must not include punctuation symbol, digit, upper and lower case")


    @field_validator('age')
    @classmethod
    def validate_number(cls, value):
        if value >= 0:
            return value
        else:
            raise ValueError("Numbers must be positive")


    @field_validator('phone')
    @classmethod
    def validate_phone(cls, value):
        if any(d in value for d in string.digits):    # digits: 0123456789
            if value[0] == '+':
                return value
        raise ValueError("Phone number start with + and only digits")


check_users = [User(**user) for user in json.load(open("users.json"))]
print(check_users)
         
