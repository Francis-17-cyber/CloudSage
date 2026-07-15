from fastapi import FastAPI

app = FastAPI(
    title="CloudSage API",
    description="AI-powered cloud infrastructure intelligence platform",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "application": "CloudSage",
        "status": "running",
        "version": "0.1.0",
        "message": "Welcome to CloudSage!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }