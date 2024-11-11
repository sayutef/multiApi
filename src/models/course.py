from sqlalchemy import Column, BigInteger, String
from src.db.base_class import Base

class Course(Base):
    id = Column(BigInteger, primary_key=True, index=True)
    name =Column(String)
    description = Column(String) 
   