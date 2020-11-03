from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.declarative import *
from sqlalchemy.orm import *
from sqlalchemy import *

Base = declarative_base()


def ConnectToDB():
	engine = create_engine('mysql+mysqldb://root:vjpvjp123A01@localhost/PxK_team?charset=utf8mb4')
	Session = sessionmaker(bind=engine)
	return Session


class Apartments(Base):
	__tablename__ = 'apartments'
	id = Column(Integer, primary_key=True)
	tileProduct = Column(String)
	date = Column(String)
	images = Column(String)
	acreage = Column(Float)
	investor = Column(String)
	juridical = Column(String)
	price = Column(Float)
	numBedroom = Column(Float)
	furniture = Column(String)
	numBathroom = Column(Float)
	description = Column(String)
	nameProject = Column(String)
	address = Column(String)
	farCenter = Column(Float)
	lat = Column(Float)
	long = Column(Float)


