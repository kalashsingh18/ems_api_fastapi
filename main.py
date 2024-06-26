from fastapi import FastAPI
from database import get_db,engine
from  routers.user import router_user
from routers.post import router_post
from routers.votes import router_votes
import models
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()
     # Add the frontend URL

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


get_db()
models.base.metadata.create_all(bind=engine)
app.include_router(router_user)
app.include_router(router_post)
app.include_router(router_votes)

print("connected")
