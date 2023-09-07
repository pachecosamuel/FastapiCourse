from fastapi import FastAPI

app = FastAPI()

@app.get("/check-health")
def health_check():
    return True