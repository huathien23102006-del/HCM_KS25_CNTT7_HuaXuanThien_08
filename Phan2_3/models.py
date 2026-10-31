from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Species(Base):
    __tablename__ = "species"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)

    pets = relationship("Pet", back_populates="species", cascade="all, delete-orphan")

class Pet(Base):
    __tablename__ = "pets"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    pet_code = Column(String(10), unique=True, nullable=False)
    price = Column(Float, nullable=False)
    species_id = Column(Integer, ForeignKey("species.id"), nullable=False)

    species = relationship("Species", back_populates="pets")