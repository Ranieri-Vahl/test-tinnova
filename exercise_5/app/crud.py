from datetime import datetime

from app import models, schemas
from app.utils import validate_brand
from fastapi import HTTPException
from sqlalchemy.orm import Session


def create_vehicle(db: Session, vehicle: schemas.VehicleCreate):
    validate_brand(vehicle.marca)
    db_vehicle = models.VehicleDB(**vehicle.model_dump())
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle


def get_vehicle(db: Session, vehicle_id: int):
    db_vehicle = db.query(models.VehicleDB).filter(models.VehicleDB.id == vehicle_id).first()
    if not db_vehicle:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")

    return db_vehicle


def get_vehicles(db: Session, skip: int = 0, limit: int = 100, brand: str = None, color: str = None, year: int = None):
    query = db.query(models.VehicleDB)
    if brand:
        query = query.filter(models.VehicleDB.marca.ilike(f"%{brand}%"))
    if color:
        query = query.filter(models.VehicleDB.cor.ilike(f"%{color}%"))
    if year:
        query = query.filter(models.VehicleDB.ano == year)
    return query.offset(skip).limit(limit).all()


def update_vehicle(db: Session, vehicle_id: int, vehicle: schemas.VehicleUpdate):
    db_vehicle = db.query(models.VehicleDB).filter(models.VehicleDB.id == vehicle_id).first()
    if not db_vehicle:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")

    vehicle_data = vehicle.model_dump(exclude_unset=True)
    if "marca" in vehicle_data:
        validate_brand(vehicle_data["marca"])

    for key, value in vehicle_data.items():
        setattr(db_vehicle, key, value)

    db_vehicle.updated = datetime.now()
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle


def update_vehicle_full(db: Session, vehicle_id: int, vehicle: schemas.VehicleCreate):
    db_vehicle = db.query(models.VehicleDB).filter(models.VehicleDB.id == vehicle_id).first()
    if not db_vehicle:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")

    validate_brand(vehicle.marca)
    db_vehicle.veiculo = vehicle.veiculo
    db_vehicle.marca = vehicle.marca
    db_vehicle.ano = vehicle.ano
    db_vehicle.descricao = vehicle.descricao
    db_vehicle.vendido = vehicle.vendido
    db_vehicle.cor = vehicle.cor
    db_vehicle.updated = datetime.now()
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle


def delete_vehicle(db: Session, vehicle_id: int):
    db_vehicle = db.query(models.VehicleDB).filter(models.VehicleDB.id == vehicle_id).first()
    if not db_vehicle:
        raise HTTPException(status_code=404, detail="Veículo não encontrado")

    db.delete(db_vehicle)
    db.commit()
    return db_vehicle
