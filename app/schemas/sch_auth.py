from pydantic import BaseModel, Field, EmailStr

class RegisterRequest(BaseModel):
    username: str = Field(..., example="иваниванов")
    email: EmailStr = Field(..., example="иваниванов@test.com")
    password: str = Field(..., min_length=6, example="securepassword")

class LoginRequest(BaseModel):
    email: str = Field(..., example="иваниванов@test.com")
    password: str = Field(..., example="securepassword")


class AuthResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    token: str = Field(..., example="mock-token")

    class Config:
        orm_mode = True