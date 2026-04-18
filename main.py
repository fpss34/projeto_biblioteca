from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
import models
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/db-test")
def test_db(db: Session = Depends(get_db)):
 try:
 db.execute(text("SELECT 1"))
 return {"status": "ok", "mensagem": "Conectado ao MariaDB com sucesso!"}
 except Exception as e:
 raise HTTPException(status_code=500, detail=str(e))


@app.post("/livros/")
def criar_livro(livro: dict, db: Session = Depends(get_db)):
    novo = models.Livro(**livro)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@app.get("/livros/")
def listar_livros(db: Session = Depends(get_db)):
    return db.query(models.Livro).all()


@app.get("/livros/{id}")
def buscar_livro(id: int, db: Session = Depends(get_db)):
    return db.query(models.Livro).filter(models.Livro.id == id).first()

@app.delete("/livros/{id}")
def deletar_livro(id: int, db: Session = Depends(get_db)):
    livro = db.query(models.Livro).filter(models.Livro.id == id).first()
    db.delete(livro)
    db.commit()
    return {"mensagem": "Livro removido"}

