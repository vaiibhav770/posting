@app.post("/create")
def create_patient(patient: Patient):

    data = load_data()

    # Check if patient ID already exists
    if patient.id in data:
        raise HTTPException(
            status_code=400,
            detail="Patient already exists"
        )

    # Add patient
    data[patient.id] = patient.model_dump()

    # Save updated data
    with open("patient.json", "w") as f:
        json.dump(data, f, indent=4)

    return {
        "message": "Patient created successfully",
        "patient": patient.model_dump()
    }