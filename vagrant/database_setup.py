from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(32), index=True)
    password_hash = Column(String(64))

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)



class UserInfo(Base):
    __tablename__ = 'user_info'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))

     @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'email': self.email
        }

class Manufacturer(Base):
    __tablename__ = 'manufacturer'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    corporate_city = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'corporate_city': self.corporate_city,
            'id': self.id,
        }

class Software(Base):
    __tablename__ = 'software'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    price = Column(String(10)))
    year_published = Column(Integer)
    manufacturer_id = Column(Integer, ForeignKey('manufacturer.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'price': self.price,
            'year_published': self.year_published,
            'id': self.id,
        }

engine = create_engine('sqlite:///softwarecatalog.db')


Base.metadata.create_all(engine)