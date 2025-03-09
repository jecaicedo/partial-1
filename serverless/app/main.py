from fastapi import FastAPI, Response
from mangum import Mangum
import json

app = FastAPI()

@app.get("/api/five_attributes", response_class=Response)
def get_five_attributes():
    five_attributes = {
            "name": "John",
            "age": "30",
            "city": "New York",
            "country": "USA",
            "occupation": "Engineer"
        }
    return Response(content=json.dumps(five_attributes), media_type="application/json")

@app.get("/api/ten_attributes", response_class=Response)
def get_ten_attributes():
    ten_attributes = {
            "name": "John",
            "age": "30",
            "city": "New York",
            "country": "USA",
            "occupation": "Engineer",
            "company": "TechCorp",
            "email": "john.doe@example.com",
            "phone": "123-456-7890",
            "gender": "Male",
            "status": "Single"
        }
    return Response(content=json.dumps(ten_attributes), media_type="application/json")

handler = Mangum(app)
