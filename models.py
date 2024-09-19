from typing import List, Optional
from uuid import UUID, uuid4
from pydantic import BaseModel
from enum import Enum

# Define Gender Enum
class Gender(str, Enum):
    MALE = "Male"
    FEMALE = "Female"

# Define Role Enum
class Role(str, Enum):
    ADMIN = "Admin"
    USER = "User"
    MODERATOR = "Moderator"

class User(BaseModel):
    id: UUID = uuid4()  # Default factory should be used with `default_factory` not direct function call
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    gender: Gender
    roles: List[Role]
