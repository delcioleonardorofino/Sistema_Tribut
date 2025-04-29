from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from db import Base


#Classes

class Cliente(Base):
    __tablename__ = "clientes"
    
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    numero = Column(String, unique=True, nullable=False)
    plano = Column (String)
    consumo = Column(Float)
    saldo = Column(Float, default=100.0)  # saldo inicial
    cdrs = relationship("CDR", back_populates="cliente") 
    
class CDR(Base):
    __tablename__ = "cdrs"

    id = Column(Integer, primary_key=True)
    numero_chamador = Column(String, nullable=False)
    numero_chamado = Column(String, nullable=False)
    inicio = Column(DateTime, nullable=False)
    fim = Column(DateTime, nullable=False)
    duracao = Column(Integer)  # em minutos
    tipo_servico = Column(String, nullable=False)  # voz, sms, dados
    quantidade = Column(Float, nullable=False)  # minutos, sms ou MB
    custo = Column(Float, nullable=False)
    cliente_id = Column(Integer, ForeignKey("clientes.id"))
    cliente = relationship("Cliente", back_populates="cdrs")
    