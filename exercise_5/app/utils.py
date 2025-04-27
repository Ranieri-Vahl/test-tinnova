from collections import defaultdict
from datetime import datetime, timedelta

from app import models
from fastapi import HTTPException
from sqlalchemy.orm import Session

VALID_BRANDS = [
    "Honda",
    "Ford",
    "Toyota",
    "Chevrolet",
    "Volkswagen",
    "Fiat",
    "Hyundai",
    "Nissan",
    "Renault",
    "Peugeot"
]


def validate_brand(brand: str):
    if brand not in VALID_BRANDS:
        raise HTTPException(status_code=400, detail=f"Marca inválida. Marcas aceitas: {', '.join(VALID_BRANDS)}")


def calculate_statistics(db: Session):
    vehicles = db.query(models.VehicleDB).all()

    total_not_sold = sum(not v.vendido for v in vehicles)

    vehicles_by_decade = defaultdict(int)
    vehicles_by_brand = defaultdict(int)
    vehicles_created_last_week = 0

    today = datetime.now()
    seven_days_ago = today - timedelta(days=7)

    for vehicle in vehicles:
        decade = (vehicle.ano // 10) * 10
        vehicles_by_decade[decade] += 1

        vehicles_by_brand[vehicle.marca] += 1

        if vehicle.created >= seven_days_ago:
            vehicles_created_last_week += 1

    return {
        "total_not_sold": total_not_sold,
        "vehicles_by_decade": dict(vehicles_by_decade),
        "vehicles_by_brand": dict(vehicles_by_brand),
        "vehicles_created_last_week": vehicles_created_last_week
    }
