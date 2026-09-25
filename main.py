from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from datetime import datetime
from fraud_engine import FraudIntelligenceEngine


app = FastAPI(
    title="FraudShield AI",
    description="Financial Fraud Intelligence System",
    version="2.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# The engine is created once when the server starts.
# It warms up using synthetic historical data.
engine = FraudIntelligenceEngine(warmup_transactions=300)


class TransactionRequest(BaseModel):
    amount: float = Field(..., gt=0)
    location_changed: int = Field(0, ge=0, le=1)
    unusual_time: int = Field(0, ge=0, le=1)
    multiple_transactions: int = Field(0, ge=0, le=1)

    # Optional richer transaction information.
    transaction_id: str | None = None
    account_id: str | None = None
    location: str | None = None
    device_id: str | None = None
    merchant: str | None = None
    transaction_type: str | None = None
    receiver_id: str | None = None


@app.get("/")
def home():
    return {
        "message": "FraudShield AI backend is running",
        "status": "success",
        "version": "2.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "engine": "online",
        "synthetic_warmup": True
    }


@app.post("/detect-fraud")
def detect_fraud(data: TransactionRequest):
    result = engine.analyze_api_transaction(data.model_dump())

    return {
        "fraud_prediction": int(
            result["risk_level"] in ["HIGH", "CRITICAL"]
        ),
        "fraud_probability": round(
            result["ml_probability"] / 100,
            2
        ),
        "result": f"{result['risk_level']} - " + (
            "Fraud Suspected"
            if result["risk_level"] in ["HIGH", "CRITICAL"]
            else "Transaction Appears Safe"
        ),
        "risk_score": result["risk_score"],
        "risk_level": result["risk_level"],
        "rule_score": result["rule_score"],
        "ml_probability": result["ml_probability"],
        "anomaly": result["anomaly"],
        "graph_flag": result["graph_flag"],
        "reasons": result["reasons"],
        "transaction_id": result["transaction_id"],
        "features": {
            "amount_ratio": result["feature_amount_ratio"],
            "z_score": result["feature_z_score"],
            "rapid_count": result["rapid_count"]
        }
    }
