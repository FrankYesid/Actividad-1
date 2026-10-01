from fastapi import FastAPI

from app.api.routes import router
from app.core.config import settings

app = FastAPI(title=settings.app_name, version="1.0.0")
app.include_router(router)


@app.get("/health", tags=["estado"])
def health_check():
    return {"status": "ok", "application": settings.app_name}