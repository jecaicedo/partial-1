from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "name": "Juan Esteban",
        "age": 22,
        "city": "Armenia",
        "profession": "Developer",
        "hobby": "Play Soccer"
    }
