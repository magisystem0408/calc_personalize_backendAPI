import json

from fastapi.applications import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:19006"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/personalities/{types_name}')
async def index(types_name: str):
    json_open = open('data/personal.json', 'r')
    json_load = json.load(json_open)
    type_detail = json_load[types_name.upper()]
    return {"message": json.dumps(type_detail)}
