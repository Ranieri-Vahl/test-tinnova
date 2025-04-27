# app/main.py

from typing import List, Optional

from app import crud, schemas
from app.models import Base, SessionLocal, engine
from app.utils import calculate_statistics
from fastapi import Depends, FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API de Veículos - Teste Tinnova"
)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    formatted_errors = []

    for error in errors:
        field = error.get("loc")[-1]
        formatted_errors.append(f"Campo '{field}' é obrigatório")

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"errors": formatted_errors}
    )


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/veiculos/", response_model=schemas.Vehicle)
def create_vehicle(vehicle: schemas.VehicleCreate, db: Session = Depends(get_db)):
    return crud.create_vehicle(db=db, vehicle=vehicle)


@app.get("/veiculos/", response_model=List[schemas.Vehicle])
def list_vehicles(
    marca: Optional[str] = None,
    cor: Optional[str] = None,
    ano: Optional[int] = None,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return crud.get_vehicles(db=db, skip=skip, limit=limit, brand=marca, color=cor, year=ano)


@app.get("/veiculos/{veiculo_id}", response_model=schemas.Vehicle)
def get_vehicle(veiculo_id: int, db: Session = Depends(get_db)):
    return crud.get_vehicle(db, veiculo_id)


@app.patch("/veiculos/{veiculo_id}", response_model=schemas.Vehicle)
def update_vehicle(veiculo_id: int, vehicle: schemas.VehicleUpdate, db: Session = Depends(get_db)):
    return crud.update_vehicle(db, veiculo_id, vehicle)


@app.delete("/veiculos/{veiculo_id}", response_model=schemas.Vehicle)
def delete_vehicle(veiculo_id: int, db: Session = Depends(get_db)):
    return crud.delete_vehicle(db, veiculo_id)


@app.put("/veiculos/{veiculo_id}", response_model=schemas.Vehicle)
def update_vehicle_full(veiculo_id: int, vehicle: schemas.VehicleCreate, db: Session = Depends(get_db)):
    return crud.update_vehicle_full(db, veiculo_id, vehicle)


@app.get("/estatisticas/")
def statistics(db: Session = Depends(get_db)):
    return calculate_statistics(db)
