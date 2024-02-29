from sqlmodel import Field, SQLModel


class Person(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    surname: str
    age: int | None = None
    city: str


class Car(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    license_plate: str = Field(index=True)
    brand: str
    model: str
    engine_cc: int
    person_id: int | None = Field(default=None, foreign_key="person.id")




