from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine, func
from flask_login import UserMixin


engine = create_engine('sqlite:///note_app.db', echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class User(Base, UserMixin):
    __tablename__ = 'users'

    id = Column('id', Integer, primary_key=True)
    email = Column('email', String(150), unique=True, nullable=False)
    password = Column('password', String(500), nullable=False)
    first_name = Column('first_name', String(150), nullable=False)
    notes = relationship('Note')

    def __init__(self, email, password, first_name):
        self.email = email
        self.password = password
        self.first_name = first_name

    def __repr__(self):
        return f'{self.id} {self.email} {self.first_name}'


class Note(Base):
    __tablename__ = 'notes'

    id = Column('id', Integer, primary_key=True)
    text = Column('text', String(10000), nullable=False)
    date = Column('date', TIMESTAMP(timezone=True), default=func.now())
    user_id = Column('user_id', Integer, ForeignKey('users.id'))

    def __init__(self, text, user_id):
        self.text = text
        self.user_id = user_id

    def __repr__(self):
        return f'{self.id} {self.text} {self.date}'


Base.metadata.create_all(bind=engine)
