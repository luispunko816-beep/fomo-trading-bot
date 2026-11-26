
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="FOMO AI TRADING API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "name": "FOMO AI TRADING",
        "status": "online"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
