from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel,Field
from typing import Optional,Annotated

import json

app=FastAPI()

class patient(BaseModel):
    id: Annotated[str,Field(...,description='Id of the patient',examples='['P001]')]
    name: Annotated[str,Field(...,description='name of the patient')]
    city: Annotated[str,Filed]
    age:
    gender:
    height:
    weight:
    bmi:
    verdict:


def load_data():
    with open('patient.json','r') as f:
        data=json.load(f)
        