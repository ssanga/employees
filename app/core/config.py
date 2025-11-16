from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Employees API"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "CRUD API for managing employees"
    DATABASE_URL: str = "sqlite:///./employees.db"
    
    class Config:
        case_sensitive = True

settings = Settings()
