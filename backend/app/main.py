from fastapi import FastAPI
from app.endpoints import syllabus, evaluation

app = FastAPI(title="POC - Introducción a la IA Generativa")

app.include_router(syllabus.router, prefix="/api/syllabus")
app.include_router(evaluation.router, prefix="/api/evaluation")

@app.get("/")
def root():
    return {"message": "POC de Introducción a la IA Generativa funcionando!"}
