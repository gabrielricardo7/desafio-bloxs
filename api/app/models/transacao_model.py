from dataclasses import dataclass
from datetime import datetime

from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer

from app.configs.database import db


@dataclass
class Transacao(db.Model):
    __tablename__ = "transacao"

    id_transacao: int = Column(Integer, primary_key=True)
    id_conta: int = Column(
        Integer,
        ForeignKey("conta.id_conta"),
        nullable=False,
    )
    valor: float = Column(Float, nullable=False)
    data_transacao: str = Column(DateTime, default=datetime.now())
    deposito: str = Column(Boolean, nullable=False)
