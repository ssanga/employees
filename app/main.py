from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.core.config import settings
from app.api.employees import router as employees_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.DESCRIPTION,
    version=settings.VERSION
)

app.include_router(employees_router)

@app.get("/", include_in_schema=False)
def root():
    """Redirect to API documentation"""
    return RedirectResponse(url="/docs")
