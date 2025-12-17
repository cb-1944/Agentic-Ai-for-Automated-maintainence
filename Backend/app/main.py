from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.graph import graph
from app.api import schedule_chat

app = FastAPI(title="Vehicle Health Backend")

# CORS (required for frontend + browser calls)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Hackathon-safe
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(
    schedule_chat.router,
    tags=["Scheduling Chat"]
)

@app.get("/", tags=["Health"])
def health():
    return {"status": "Backend running"}

@app.post("/run-diagnosis", tags=["Diagnosis"])
def run_diagnosis(telemetry: dict):
    """
    Runs anomaly detection, diagnosis, and engagement
    on incoming telemetry (mock / IoT simulated).
    """
    result = graph.invoke({
        "telemetry": telemetry
    })
    return result
