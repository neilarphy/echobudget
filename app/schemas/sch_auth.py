from pydantic import BaseModel, Field, EmailStr

class RegisterRequest(BaseModel):
    username: str = Field(..., example="иваниванов")
    email: EmailStr = Field(..., example="иваниванов@example")
    password: str = Field(..., min_length=6, example="securepassword")

class LoginRequest(BaseModel):
    username: str = Field(..., example="иваниванов")
    password: str = Field(..., example="securepassword")


class AuthResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    token: str = Field(..., example="mock-token")

    class Config:
        orm_mode = True