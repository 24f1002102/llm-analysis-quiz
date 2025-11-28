from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from solver.quiz_solver import solve_quiz  # now sync

app = FastAPI()

# Store your correct secret here
STUDENT_SECRET = "abc123"

class QuizRequest(BaseModel):
    email: str
    secret: str
    url: str

@app.post("/")
def receive_quiz(req: QuizRequest):
    # Validate secret
    if req.secret != STUDENT_SECRET:
        raise HTTPException(status_code=403, detail="Invalid secret")

    # Solve the quiz (synchronous now)
    try:
        answer = solve_quiz(req.url, req.email, req.secret)
        return {
            "email": req.email,
            "url": req.url,
            "answer": answer
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
