from fastapi import FastAPI, HTTPException  # Corrected HTTPException import
from typing import List
from uuid import UUID, uuid4
from models import User, Gender, Role  # Fixed import statement

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(),
        first_name="Jamila",  # Correct field name
        last_name="Ahmed",
        gender=Gender.FEMALE,
        roles=[Role.ADMIN, Role.USER]  # Added a comma
    ),
    User(
        id=uuid4(),
        first_name="John",  # Correct field name
        last_name="Doe",
        gender=Gender.MALE,
        roles=[Role.USER]
    )
]

@app.get("/")
async def root():
    return {"Hello": "World"}

@app.get("/api/v1/users")
async def fetch_users():
    return db  # Removed the unnecessary semicolon

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": "User deleted successfully"}
    raise HTTPException(  # Corrected to HTTPException
        status_code=404,
        detail=f"User with id: {user_id} does not exist"
    )

@app.put("/api/v1/users/{user_id}")
async def update_user(user_id: UUID, user_data: User):
    for user in db:
        if user.id == user_id:
            user.first_name = user_data.first_name
            user.last_name = user_data.last_name
            user.gender = user_data.gender
            user.roles = user_data.roles
            return {"message": "User updated successfully", "user": user}
    
    # If the user is not found, raise an HTTPException
    raise HTTPException(
        status_code=404,
        detail=f"User with id: {user_id} does not exist"  # Fixed string termination
    )
