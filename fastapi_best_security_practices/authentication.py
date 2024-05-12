from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
@app.post("/token")
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    # Replace with your DB check
    if form_data.username != "user" or form_data.password != "secret":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    # Return a token here
    return {"access_token": "your_token", "token_type": "bearer"}


@app.get("/users/me")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    return {"token": token}