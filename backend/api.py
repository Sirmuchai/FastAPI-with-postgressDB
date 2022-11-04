from fastapi import  FastAPI

app = FastAPI()

@app.get("/")
def hellow():
    return {"key":"greetings",
            "value": "Hello tp you"}