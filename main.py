from fastapi import FastAPI

app = FastAPI(
    title="Farm Manager API",
    description="API for the Farm Manager application",
    version="0.1.0",
)

@app.get("/ol")
def read_root():
    temp = "This is great and funny at the same time"
    return temp

@app.get("/health")
def health_check():
    return {"status": "healthy"}
