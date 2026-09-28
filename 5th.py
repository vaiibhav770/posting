from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel,Field,computed_field
from typing import Optional,Annotated,Literal

import json

app=FastAPI()

class patient(BaseModel):
    id: Annotated[str, Field(..., description='Id of the patient', examples='['P001'])]
    name: Annotated[str, Field(..., description='name of the patient')]
    city: Annotated[str, Filed(..., description='city of the patient')]
    age: Annotation[int, Field(..., gt=0, lt=120, description='age must be a number')]
    gender: Annotated[Literal['male','female','other'], Field(..., description='choose between Male or female')]
    height: Annotated[float, Field(..., gt=0 description='enter height of the patient')]
    weight: Annotated[float, Field(..., gt=0, description='enter weight of the patient')]

    @computed_field
    @property
    def bmi(self) -> float:
    bmi =round(self.weight/(self.height**2),2)
    return bmi

    @computed_field
    @property
    def verdict(self) -> str:
    if self.bmi < 18.5:
    return 'under weight'
    elif self.bmi < 25:
    return 'normal'
    elif self.bmi <30:
    return 'normal'
    


def load_data():
    with open('patient.json','r') as f:
        data=json.load(f)
        
    return data


@app.get("/")
def hello():