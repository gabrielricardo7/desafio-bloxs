from dataclasses import dataclass

from sqlalchemy import Column, Date, Integer, String

from app.configs.database import db


@dataclass
class Pessoa(db.Model):
    __tablename__ = "pessoa"

    id_pessoa: int = Column(Integer, primary_key=True)
    nome: str = Column(String(255), nullable=False)
    cpf: str = Column(String(11), nullable=False, unique=True)
    data_nascimento: str = Column(Date, nullable=False)
