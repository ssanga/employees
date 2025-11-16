from sqlalchemy import Column, Integer, String, Float, Date
from app.core.database import Base

class Employee(Base):
    __tablename__ = "employees"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    department = Column(String, nullable=False)
    salary = Column(Float, nullable=False)
    hire_date = Column(Date, nullable=False)
