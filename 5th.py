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
    height: Annotated[float, Field(..., gt=0, description='enter height of the patient')]
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
    else:
    return 'obese'
    


def load_data():
    with open('patient.json','r') as f:
        data=json.load(f)
        
    return data


@app.get("/")
def hello():
return {'message':'Patient management system api'}

@app.get('/about')
def about():
return {'message':'A fully functional api to manage your patient records'}

@app.get('/patient/{patient_id}')
def view_patient(patient_id:str=path(...,description='id of the patient in the DB',example='P001')):
    sort_by: str = Query("name", description="Field to sort by")
    order: str = Query("asc", description="asc or desc")
):
    data = load_data()

    if sort_by not in ["age", "height", "weight", "bmi", "name"]:
        raise HTTPException(
            status_code=400,
            detail="Invalid sort field"
        )

    if order not in ["asc", "desc"]:
        raise HTTPException(
            status_code=400,
            detail="Order must be asc or desc"
        )

    patients = list(data.values())

    if sort_by == "bmi":
        patients.sort(
            key=lambda patient: patient["weight"] / (patient["height"] ** 2),
            reverse=(order == "desc")
        )
    else:
        patients.sort(
            key=lambda patient: patient[sort_by],
            reverse=(order == "desc")
        )

    return patients



