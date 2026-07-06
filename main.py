from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def health_check():
    return {"status": "healthy"}

@app.get("/test")
def test_endpoint():
    return {"message": "This is a test response."}
