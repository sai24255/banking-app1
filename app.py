from fastapi import FastAPI

app = FastAPI(title="Banking App")

@app.get("/")
def home():
    return {
        "application": "banking-app",
        "status": "running",
        "environment": "development"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
