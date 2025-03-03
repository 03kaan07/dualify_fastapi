from fastapi import FastAPI, HTTPException
from dualis.dualis import run_noten_script
from models.schema import LoginRequest

app = FastAPI()

@app.post("/grades", summary="Retrieves all existing grades using your email and password (it takes some time when it works)")
async def get_grades(data: LoginRequest):
    if not data.username or not data.password:
        raise HTTPException(status_code=400, detail="Username and password cannot be empty")
    
    result = run_noten_script(data.username, data.password)
    return result
