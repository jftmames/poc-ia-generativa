from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.utils.ia_integration import generate_syllabus

router = APIRouter()

class SyllabusRequest(BaseModel):
    prompt: str

@router.post("/")
async def create_syllabus(data: SyllabusRequest):
    try:
        syllabus_text = generate_syllabus(data.prompt)
        return {"syllabus": syllabus_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
