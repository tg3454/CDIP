# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from engine import calculate_pollution, generate_option_c, compare_options, explain_reason
from ml_model import confidence_score

app = FastAPI(title="CDIP - Climate Decision Intelligence Platform")

# CORS (to connect with HTML frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    optionA: str
    optionB: str
    months: int


@app.post("/analyze")
def analyze(data: InputData):

    pollA, qtyA, devA = calculate_pollution(data.optionA, data.months)
    pollB, qtyB, devB = calculate_pollution(data.optionB, data.months)

    optionC_text, pollC = generate_option_c(data.optionA, data.optionB, data.months)

    status, percent = compare_options(pollA, pollB)

    reason = explain_reason(devA, devB)

    return {
        "optionA": {"text": data.optionA, "pollution": pollA},
        "optionB": {"text": data.optionB, "pollution": pollB},
        "optionC": {"text": optionC_text, "pollution": pollC},
        "comparison": f"Option A is {percent}% {status} than Option B.",
        "reason": reason,
        "confidence": confidence_score()
    }
