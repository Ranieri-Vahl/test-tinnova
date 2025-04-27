from datetime import datetime

from sqlalchemy import (Boolean, Column, DateTime, Integer, String,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class VehicleDB(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    veiculo = Column(String, index=True)
    marca = Column(String, index=True)
    ano = Column(Integer)
    descricao = Column(String)
    vendido = Column(Boolean, default=False)
    created = Column(DateTime, default=datetime.now())
    updated = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    cor = Column(String)


def init_db():
    Base.metadata.create_all(bind=engine)
