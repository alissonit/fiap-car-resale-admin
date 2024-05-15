from fastapi import FastAPI

from src.adapters.driving.rest.v1.cars import router as cars_router
from src.adapters.driving.rest.v1.users import router as users_router
from src.adapters.driving.rest.v1.login import router as login_router
from src.adapters.driving.rest.v1.settings import router as settings_router
from src.configuration.dependency_injection import Container


container = Container()

app = FastAPI(
    title="Resale Car API",
    description="API for managing cars for resale",
    version="1.0.0",
    openapi_url="/api/v1/openapi.json",
    docs_url="/api/v1/docs",
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    }
)



@app.get("/api/v1/health")
async def health():
    return {"status": "ok"}

app.include_router(login_router, tags=["login"])
app.include_router(users_router, tags=["users"])
app.include_router(cars_router, tags=["cars"])
app.include_router(settings_router, tags=["settings"])
