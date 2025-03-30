from fastapi import FastAPI, HTTPException
from dualis.dualis import dualis_main
from models.schema import LoginRequest

app = FastAPI()

@app.post("/grades/{semester}", summary="Retrieves all existing grades of a specified semester (1-6) using your email and password (it takes some time when it works)")
async def get_grades(data: LoginRequest, semester: int):
    if not data.username or not data.password:
        raise HTTPException(status_code=400, detail="Username and password cannot be empty")
    
    result = dualis_main(data.username, data.password, semester)
    return result
