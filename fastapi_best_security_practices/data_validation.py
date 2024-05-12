from pydantic import BaseModel, EmailStr
from authentication import app


class User(BaseModel):
    username: str
    email: EmailStr
    full_name: str = None


@app.post("/user/", response_model=User)
async def create_user(user: User):
    return user