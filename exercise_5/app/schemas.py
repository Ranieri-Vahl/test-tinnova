# app/schemas.py

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class VehicleBase(BaseModel):
    veiculo: str = Field(description="Modelo do veículo", example="Civic")
    marca: str = Field(description="Fabricante do veículo", example="Honda")
    ano: int = Field(description="Ano de fabricação", example=2020)
    descricao: str = Field(description="Descrição do veículo", example="Sedan")
    vendido: bool = Field(default=False, description="Status de venda do veículo")
    cor: str = Field(..., description="Cor do veículo", example="Preto")


class VehicleCreate(VehicleBase):
    pass


class VehicleUpdate(BaseModel):
    veiculo: Optional[str] = Field(None, description="Modelo do veículo", example="Civic")
    marca: Optional[str] = Field(None, description="Fabricante do veículo", example="Honda")
    ano: Optional[int] = Field(None, description="Ano de fabricação", example=2020)
    descricao: Optional[str] = Field(None, description="Descrição do veículo", example="Sedan")
    vendido: Optional[bool] = Field(None, description="Status de venda do veículo")
    cor: Optional[str] = Field(None, description="Cor do veículo", example="Preto")


class Vehicle(VehicleBase):
    id: int = Field(description="ID único do veículo", example=1)
    created: datetime = Field(description="Data de criação")
    updated: datetime = Field(description="Data de última atualização")
