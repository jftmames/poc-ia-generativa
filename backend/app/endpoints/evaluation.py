from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.utils.nlp import compute_embedding, compare_embeddings

router = APIRouter()

class EvaluationRequest(BaseModel):
    student_response: str
    reference_text: str

@router.post("/")
async def evaluate_response(data: EvaluationRequest):
    try:
        emb_student = compute_embedding(data.student_response)
        emb_reference = compute_embedding(data.reference_text)
        similarity = compare_embeddings(emb_student, emb_reference)
        return {"similarity": similarity}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
