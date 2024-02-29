from sqlmodel import Session, select
from persone_Maccione import Person, Car

persone = []

def create_person(engine):
    with Session(engine) as session:
       # Create 5 Person instances
        person1 = Person(name="John", surname="Doe", age=30, city="New York")
        person2 = Person(name="Jane", surname="Doe", age=28, city="Los Angeles")
        person3 = Person(name="Alice", surname="Smith", age=35, city="Chicago")
        person4 = Person(name="Bob", surname="Johnson", age=40, city="Houston")
        person5 = Person(name="Charlie", surname="Brown", age=50, city="Phoenix")
        session.add(person1)
        persone.append(person1)
        session.add(person2)
        persone.append(person2)
        session.add(person3)
        persone.append(person3)
        session.add(person4)
        persone.append(person4)
        session.add(person5)
        persone.append(person5)    
        session.commit()

        session.refresh(person1)
        session.refresh(person2)
        session.refresh(person3)
        session.refresh(person4)
        session.refresh(person5)



def select_person_cars(engine, person_name):
    with Session(engine) as session:

        statement = select(Person,Car).where(Person.name == person_name).where(Person.id == Car.person_id)
        result = session.exec(statement)
        person_jhon = result.all()
        print(person_jhon[0][0],"\n\n")
        for _ in person_jhon:
            print(_[1]) 
        #print("John's car again:", person_jhon.car)


def create_car(engine):
    with Session(engine) as session:
        
    # Create 10 Car instances
        car1 = Car(license_plate="ABC123", brand="Toyota", model="Corolla", engine_cc=1800, person_id=persone[0].id)
        car2 = Car(license_plate="DEF456", brand="Honda", model="Civic", engine_cc=2000, person_id=persone[1].id)
        car3 = Car(license_plate="GHI789", brand="Ford", model="Mustang", engine_cc=5000, person_id=persone[2].id)
        car4 = Car(license_plate="JKL012", brand="Chevrolet", model="Camaro", engine_cc=6200, person_id=persone[3].id)
        car5 = Car(license_plate="MNO345", brand="BMW", model="M3", engine_cc=3000, person_id=persone[4].id)
        car6 = Car(license_plate="PQR678", brand="Audi", model="A4", engine_cc=2000, person_id=persone[0].id)
        car7 = Car(license_plate="STU901", brand="Mercedes", model="C Class", engine_cc=2000, person_id=persone[1].id)
        car8 = Car(license_plate="VWX234", brand="Porsche", model="911", engine_cc=3000, person_id=persone[2].id)
        car9 = Car(license_plate="YZA567", brand="Lamborghini", model="Huracan", engine_cc=5200, person_id=persone[3].id)
        car10 = Car(license_plate="BCD890", brand="Ferrari", model="488", engine_cc=3900, person_id=persone[4].id)
        session.add(car1)
        session.add(car2)
        session.add(car3)
        session.add(car4)
        session.add(car5)
        session.add(car6) 
        session.add(car7)
        session.add(car8)
        session.add(car9)
        session.add(car10)      
        session.commit()

        session.refresh(car1)
        session.refresh(car2)
        session.refresh(car3)
        session.refresh(car4)
        session.refresh(car5)
        session.refresh(car6)
        session.refresh(car7)
        session.refresh(car8)
        session.refresh(car9)
        session.refresh(car10)
