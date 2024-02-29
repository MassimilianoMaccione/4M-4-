import os
from database_Maccione import create_db_and_tables, create_engine_with_db
from crud_Maccione import (
    create_person,
    select_person
    )


def main():
    db_name = "database.db"
    verbose = False
    delete_database = True
    if delete_database:
        try:
            os.remove(db_name)
        except FileNotFoundError:
            print(f"{db_name} not found")

    engine = create_engine_with_db(db_name, verbose)
    create_db_and_tables(engine)
    create_person(engine)
    select_person(engine)
    #update_person(engine)
    #delete_person(engine)


if __name__ == "__main__":
    main()
    # TODO https://sqlmodel.tiangolo.com/tutorial/many-to-many/link-with-extra-fields/
