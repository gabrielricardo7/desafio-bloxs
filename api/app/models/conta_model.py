from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer

from app.configs.database import db


@dataclass
class Conta(db.Model):
    __tablename__ = "conta"

    id_conta: int = Column(Integer, primary_key=True)
    id_pessoa: int = Column(
        Integer,
        ForeignKey("pessoa.id_pessoa"),
        nullable=False,
    )
    saldo: float = Column(Float)
    limite_saque_diario: float = Column(Float)
    flag_ativo: bool = Column(Boolean, default=True)
    tipo_conta: int = Column(Integer)
    data_criacao: str = Column(DateTime, default=datetime.now())
