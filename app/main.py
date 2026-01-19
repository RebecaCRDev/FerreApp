from fastapi import FastAPI

app = FastAPI(
    title="FerreApp API",
    version="1.0.0",
    description="API for managing ferreteria operations"
)

@app.get("/ping")
def ping():
    return {"message": "pong!"}