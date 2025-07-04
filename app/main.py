import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Welcome to Orderin!"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", reload=True)