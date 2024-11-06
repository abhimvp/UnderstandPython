from sqlalchemy import create_engine, ForeignKey, Column, Integer, String, CHAR

# String , Integer , CHAR are data types for Column
# create_engine is used to create a connection to the database we can connect to
# because sqlchemy is compatible with a bunch of different databases like sqllite , mysql
# In this we use sqllite
from sqlalchemy.ext.declarative import declarative_base

# Construct a base class for declarative class definitions.
#     The new base class will be given a metaclass that produces
#     appropriate :class:`~sqlalchemy.schema.Table` objects and makes
#     the appropriate :class:`_orm.Mapper` calls based on the
#     information provided declaratively in the class and any subclasses
#     of the class.
# The Base Class that we're going to inherit from our person in thing class
from sqlalchemy.orm import sessionmaker

# The .sessionmaker factory generates new .Session objects when called,
# creating them given the configurational arguments established here
# we can start a session and do stuff in the database

Base = declarative_base()
# returns a class which will be a BASE for our Person CLass


class Person(Base):
    # This is the name of the table in the database
    __tablename__ = "people"
    # This is the name of the column in the database / Attributes in out table
    ssn = Column("ssn", Integer, primary_key=True)  # unique Identifier
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    gender = Column("gender", CHAR)
    age = Column("age", Integer)

    def __init__(self, ssn, firstname, lastname, gender, age):
        self.ssn = ssn
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.age = age

    def __repr__(self):
        return (
            f"({self.ssn}) {self.firstname} {self.lastname} ({self.gender}, {self.age})"
        )


# Above we create a database Table
# Now we need to create an engine to connect to the database
# & specify what database we're going to connect to
engine = create_engine("sqlite:///mydb.db", echo=True)
# this will connect to sqlite database and create a file called mydb.db & works with that file
Base.metadata.create_all(bind=engine)
# this will take all the classes that  extend from BASE we have defined and
# connects to engine and create the tables in the database
# person table will be created after above line of code runs
Session = sessionmaker(bind=engine)  # class - creates a session to do things with db
session = Session()  # instance

# person = Person(
#     1223343, "John", "Doe", "M", 30
# )  # creating a person record(object) to be inserted into table
# session.add(
#     person
# )  # this will add the info into the table - here no sql query used and this person will be created in database
# session.commit()  # this will commit/apply the changes to the database - creates the person in db

# # we can bunch of people at a time as well
# p1 = Person(123, "James", "Doe", "M", 30)
# p2 = Person(124, "Jane", "Doe", "F", 28)
# p3 = Person(125, "John", "Smith", "M", 35)
# p4 = Person(126, "Jane", "Smith", "F", 32)
# session.add_all([p1, p2, p3, p4])
# session.commit()

# we can also query the database
result = session.query(Person).all()
# this will return a list of all the people in the database
# we get python objects from the database
# print(result)
for person in result:
    print(person)

# we can also filter the query
result_filtered = session.query(Person).filter(Person.age > 30)
print("Filtered Results:", result_filtered.all())
# filter using in_ on firstnme
result_filtered_firstname = session.query(Person).filter(
    Person.firstname.in_(["John", "Jane"])
)
# result_filtered = session.query(Person).filter(Person.age.in_([30, 35]))
print("Filtered Results:", result_filtered_firstname.all())
