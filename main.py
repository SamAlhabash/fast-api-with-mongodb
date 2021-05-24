from fastapi import FastAPI
from config.config import settings
from starlette.middleware.cors import CORSMiddleware
from api.api_v1.api import api_router
from api.api_v1.services.database import connect_db, close_db
import uvicorn

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESC,
    version=settings.PROJECT_VERSION,
    openapi_url="/open-api.json",
    docs_url="/swagger",
    redoc_url="/redoc"
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin)
                       for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
app.add_event_handler("startup", connect_db)
app.add_event_handler("shutdown", close_db)
app.include_router(api_router, prefix=settings.API_V1_STR)


if __name__ == '__main__':
    uvicorn.run(app='main:app',
                host="0.0.0.0",
                port=8000,
                reload=True)
