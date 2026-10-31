from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Optional, List

from database import engine, get_db
import models
from Schemas import PetCreate, PetResponse

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Pet Shop API")

def standard_response(status_code: int, error=None, message: str = "", data=None):
    return{
        "statusCode": status_code,
        "error": error,
        "message": message,
        "data": data
    }

@app.post("pets", status_code=status.HTTP_201_CREATED)
def create_pet(pet_in: PetCreate, db: Session = Depends(get_db)):

    species = db.query(models.Species).filter(models.Species.id == pet_in.species_id).first()
    if not species:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=standard_response(400, error="Bad Request", message=f"Species với id {pet_in.species_id} không tồn tại.")
        )
    existing_pet = db.query(models.Pet).filter(models.Pet.pet_code == pet_in.pet_code).first()
    if existing_pet:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=standard_response(400, error="Bad Request", message=f"Mã thú cưng'{pet_in.pet_code}' đã tồn tại trong hệ thống!")
        )

    new_pet = models.Pet(
        pet_code=pet_in.pet_code,
        price=pet_in.price,
        species_id=pet_in.species_id
    )

    db.add(new_pet)
    db.commit()
    db.refresh(new_pet)

    pet_data = PetResponse.model_validate(new_pet).model_dump()

    return standard_response(201, message="Thêm mới thú cưng thành công", data=pet_data)