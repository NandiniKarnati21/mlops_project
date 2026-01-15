from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "DTU MLOps Cloud Run is running 🚀"}
