from fastapi import FastAPI

from fastapi import FastAPI

from app.api.routes import assessments
from app.api.routes import chat
from app.api.routes import documents
from app.api.routes import health


app = FastAPI(
    title="AyurakshaIP Backend",
    version="0.1.0",
)


app.include_router(health.router)
app.include_router(assessments.router)
app.include_router(documents.router)
app.include_router(chat.router)