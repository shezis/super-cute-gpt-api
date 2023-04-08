from fastapi import FastAPI
import src.routes.user as users

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["users"])
