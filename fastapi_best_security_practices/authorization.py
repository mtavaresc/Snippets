from fastapi import Depends, HTTPException
from .authentication import app, oauth2_scheme


def get_current_user_role(token: str = Depends(oauth2_scheme)):
    # Extract user role from the token
    return "admin"   # Simplified for illustration


def role_checker(role: str):
    def role_dependecy(user_role: str = Depends(get_current_user_role)):
        if user_role != role:
            raise HTTPException(
                status_code=403,
                detail="Operation not permitted"
            )
    return role_dependecy


@app.get("/admin")
async def admin_endpoint(user_role: str = Depends(role_checker("admin"))):
    return {"status": "Welcome Admin!"}