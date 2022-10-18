from typing import Union

from pydantic import BaseModel


class Artist(BaseModel):
    _id: Union[int, None] = None
    firstname: str
    lastname: str
    date_of_birth: str
    cover: str


def __str__(self):
    return f'firstname={self.firstname}, lastname={self.lastname},date_of_birth={self.date_of_birth},cover={self.cover}'
