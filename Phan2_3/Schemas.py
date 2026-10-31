from pydantic import BaseModel, Field, field_validator
from typing import Optional, List
import re

class SpeciesResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

# Phần 2.1
class PetCreate(BaseModel):
    pet_code: str = Field(..., min_length=4, max_length=10)
    price: float = Field(..., gt=0)
    species_id: int

    @field_validator('pet_code')
    def validate_pet_code(cls, v):
        v_cleaned = v.strip().upper()
        if not re.match(r"^P\d+$", v_cleaned):
            raise ValueError("pet_code phải bắt đầu bằng chữ P và theo sau các chữ số!")
        return v_cleaned

# Phần 2.2
class PetResponse(BaseModel):
    id: int
    pet_code: str
    price: float
    species: SpeciesResponse

    class Config:
        from_attributes = True