from sqlalchemy import Column, Integer, String
from database import Base

class Livro(Base):
    __tablename__ = "livro"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(200))
    autor = Column(String(150))
    ano = Column(Integer)
    editora = Column(String(150))
    edicao = Column(String(50))
    localizacao = Column(String(100))
