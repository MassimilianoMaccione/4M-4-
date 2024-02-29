from sqlmodel import Field, SQLModel
from typing import Optional

class Person(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    surname: str
    age: Optional[int] = None
    city: str


class Car(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    license_plate: str = Field(index=True)
    brand: str
    model: str
    engine_cc: int
    person_id: Optional[int] = Field(default=None, foreign_key="person.id")




