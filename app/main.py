import os
from app.routes import modalities
from fastapi import FastAPI
from .database import Base, engine
from .routes.routes import router
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)
app.include_router(modalities.router)

allow_origins = os.getenv("ALLOW_ORIGIN_DOMAIN")
print(allow_origins, allow_origins.split(","))
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins.split(","),
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
