from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    username: str = Field(..., example="иваниванов")
    email: EmailStr = Field(..., example="иваниванов@example")
    password: str = Field(..., min_length=6)

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr
    balance: int

    class Config:
        orm_mode = True