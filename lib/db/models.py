from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///waste.db')
Session = sessionmaker(bind=engine)
session = Session()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    waste_entries = relationship("WasteEntry", back_populates="user")

class WasteEntry(Base):
    __tablename__ = 'waste_entries'
    id = Column(Integer, primary_key=True)
    date = Column(Date)
    waste_type = Column(String)
    weight_kg = Column(Float)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="waste_entries")

class DisposalMethod(Base):
    __tablename__ = 'disposal_methods'
    id = Column(Integer, primary_key=True)
    method = Column(String)
    waste_entry_id = Column(Integer, ForeignKey('waste_entries.id'))
    waste_entry = relationship("WasteEntry")

Base.metadata.create_all(engine)