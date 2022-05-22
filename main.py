from fastapi import FastAPI
from routes import evidences

app = FastAPI()

app.include_router(evidences.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}