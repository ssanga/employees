from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class EmployeeBase(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    age: int = Field(..., gt=0, lt=120)
    department: str = Field(..., min_length=1, max_length=100)
    salary: float = Field(..., gt=0)
    hire_date: date

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    first_name: Optional[str] = Field(None, min_length=1, max_length=100)
    last_name: Optional[str] = Field(None, min_length=1, max_length=100)
    age: Optional[int] = Field(None, gt=0, lt=120)
    department: Optional[str] = Field(None, min_length=1, max_length=100)
    salary: Optional[float] = Field(None, gt=0)
    hire_date: Optional[date] = None

class EmployeeResponse(EmployeeBase):
    id: int
    
    class Config:
        from_attributes = True
