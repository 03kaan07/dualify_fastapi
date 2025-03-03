from pydantic import BaseModel, Field

class LoginRequest(BaseModel):
    username: str = Field(..., min_length=1, description="User's email or username")
    password: str = Field(..., min_length=1, description="User's password")

    class Config:
        schema_extra = {
            "example": {
                "username": "maxmustermann@student.dhbw-mannheim.de",
                "password": "abcdefghijklm"
            }
        }
