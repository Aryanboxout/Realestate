""" database dependencies to support Users db examples """
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from flask_migrate import Migrate
from __init__ import app

# Tutorial: https://www.sqlalchemy.org/library.html#tutorials, try to get into Python shell and follow along

dbURI = 'sqlite:///model/myDB.db'
# Setup properties for the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = dbURI
app.config['SECRET_KEY'] = 'SECRET_KEY'
# Create SQLAlchemy engine to support SQLite dialect (sqlite:)
db = SQLAlchemy(app)
Migrate(app, db)

# Define the Users table within the model
# -- Object Relational Mapping (ORM) is the key concept of SQLAlchemy
# -- a.) db.Model is like an inner layer of the onion in ORM
# -- b.) Users represents data we want to store, something that is built on db.Model
# -- c.) SQLAlchemy ORM is layer on top of SQLAlchemy Core, then SQLAlchemy engine, SQL
class School(db.Model):
    # define the Users schema
    userID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    number = db.Column(db.String(255), unique=True, nullable=False)
    teacher = db.Column(db.String(255), unique=False, nullable=False)
    subject = db.Column(db.String(255), unique=False, nullable=False)

    # constructor of a User object, initializes of instance variables within object
    def __init__(self, name, number, teacher, subject):
        self.name = name
        self.number = number
        self.teacher = teacher
        self.subject = subject

    # CRUD create/add a new record to the table
    # returns self or None on error
    def create(self):
        try:
            # creates a person object from Users(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "userID": self.userID,
            "name": self.name,
            "number": self.number,
            "teacher": self.teacher,
            "subject": self.subject,
            "query": "by_alc"  # This is for fun, a little watermark
        }

    # CRUD update: updates users name, password, phone
    # returns self
    def update(self, name, teacher="", subject=""):
        """only updates values with length"""
        if len(name) > 0:
            self.name = name
        if len(teacher) > 0:
            self.teacher = teacher
        if len(subject) > 0:
            self.subject = subject
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None


"""Database Creation and Testing section"""


def model_tester():
    print("--------------------------")
    print("Seed Data for Table: users")
    print("--------------------------")
    db.create_all()
    """Tester data for table"""
    u1 = School(name='Thomas Edison', number='tedison@example.com', teacher='123toby', subject="1111111111")
    u2 = School(name='Nicholas Tesla', number='ntesla@example.com', teacher='123niko', subject="1111112222")
    u3 = School(name='Alexander Graham Bell', number='agbell@example.com', teacher='123lex', subject="1111113333")
    u4 = School(name='Eli Whitney', number='eliw@example.com', teacher='123whit', subject="1111114444")
    u5 = School(name='John Mortensen', number='jmort1021@gmail.com', teacher='123qwerty', subject="8587754956")
    u6 = School(name='John Mortensen', number='jmort1021@yahoo.com', teacher='123qwerty', subject="8587754956")
    # U7 intended to fail as duplicate key
    u7 = School(name='John Mortensen', number='jmort1021@yahoo.com', teacher='123qwerty', subject="8586791294")
    table = [u1, u2, u3, u4, u5, u6, u7]
    for row in table:
        try:
            db.session.add(row)
            db.session.commit()
        except IntegrityError:
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {row.number}")


def model_printer():
    print("------------")
    print("Table: users with SQL query")
    print("------------")
    result = db.session.execute('select * from school')
    print(result.keys())
    for row in result:
        print(row)


if __name__ == "__main__":
    model_tester()
    # builds model of Users
    model_printer()
