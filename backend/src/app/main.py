from fastapi import FastAPI
import app.routers.base_access as base_access_router
import app.routers.enlisted_personnel as enlisted_personnel_router


app = FastAPI()
app.include_router(base_access_router.router)
app.include_router(enlisted_personnel_router.router)
