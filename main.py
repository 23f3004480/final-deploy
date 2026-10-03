"""
Simple FastAPI app serving a scikit-learn text classification model.

Run locally:
    uvicorn main:app --reload

Test it:
    curl -X POST http://127.0.0.1:8000/predict \
         -H "Content-Type: application/json" \
         -d '{"text": "This is a great product"}'
"""

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "model.pkl")

app = FastAPI(
    title="Getting Started with ML in Production API",
    description="A minimal sentiment prediction API built for the workshop.",
    version="1.0.0",
)

# Load the model once at startup
try:
    model = joblib.load(MODEL_PATH)
except Exception:
    model = None


class PredictionRequest(BaseModel):
    text: str = Field(
        ...,
        min_length=1,
        description="Text to classify"
    )


class PredictionResponse(BaseModel):
    prediction: int
    class_name: str


@app.get("/")
def root():
    return {
        "message": "Workshop ML API is running. See /docs for usage."
    }


@app.get("/health")
def health():
    return {
        "status": "ok",
        "model_loaded": model is not None
    }


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):

    if model is None:
        raise HTTPException(
            status_code=503,
            detail="Model not loaded. Check model.pkl and scikit-learn version."
        )

    try:
        # The pipeline expects raw text, not a NumPy feature array.
        pred = int(model.predict([request.text])[0])

        return PredictionResponse(
            prediction=pred,
            class_name=f"class_{pred}"
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {type(e).__name__}: {e}"
        )