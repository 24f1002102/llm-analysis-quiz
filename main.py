from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from solver.quiz_solver import solve_quiz

app = FastAPI()

STUDENT_SECRET = "abc123"

class QuizRequest(BaseModel):
    email: str
    secret: str
    url: str

@app.get("/")
def root():
    return {"message": "API is running!"}

@app.post("/")
def receive_quiz(req: QuizRequest):
    if req.secret != STUDENT_SECRET:
        raise HTTPException(status_code=403, detail="Invalid secret")
    try:
        answer = solve_quiz(req.url, req.email, req.secret)
        return {
            "email": req.email,
            "url": req.url,
            "answer": answer
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
