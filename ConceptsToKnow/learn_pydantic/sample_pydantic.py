from datetime import datetime

from pydantic import BaseModel, PositiveInt, ValidationError


class User(BaseModel):
    id: int  
    name: str = 'John Doe'  
    signup_ts: datetime | None  
    tastes: dict[str, PositiveInt]  


external_data ={'id': 'not an int', 'tastes': {}}

# external_data = {
#     'id': 123,
#     'signup_ts': '2019-06-01 12:22',  
#     'tastes': {
#         'wine': 9,
#         b'cheese': 7,  
#         'cabbage': '1',  
#     },
# }

# # The commented code block is attempting to create an instance of the `User` class using the data
# provided in the `external_data` dictionary.
# try:
#     User(**external_data)
# except ValidationError as e:
#     print(e.json())  

# print(user.id)  
#> 123
# print(user.model_dump())

# serialization

class Address(BaseModel):
    street: str
    city: str
    zipcode: str

class Meeting(BaseModel):
    when: datetime
    where: Address
    why: str = 'No idea'


# m = Meeting(when='2020-01-01T12:00', where='home')
# print(m.model_dump(exclude_unset=True))
# #> {'when': datetime.datetime(2020, 1, 1, 12, 0), 'where': b'home'}
# print(m.model_dump(exclude={'where'}, mode='json'))
# #> {'when': '2020-01-01T12:00:00', 'why': 'No idea'}
# print(m.model_dump_json(exclude_defaults=True))
#> {"when":"2020-01-01T12:00:00","where":"home"}


    
print(Meeting.model_json_schema())