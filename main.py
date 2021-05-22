from fastapi import FastAPI
from config import settings
from starlette.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(
    title=settings.PROJECT_NAME,
    description=settings.PROJECT_DESC,
    version=settings.PROJECT_VERSION,
    openapi_url=f"{settings.API_V1_STR}/open-api.json",
    docs_url=f"{settings.API_V1_STR}/swagger",
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


if __name__ == '__main__':
    uvicorn.run(app='main:app',
                host="0.0.0.0",
                port=8000,
                reload=True)
