from fastapi import FastAPI
import app.routers.enlisted_personnel as enlisted_personnel_router


app = FastAPI()
app.include_router(enlisted_personnel_router.router)
