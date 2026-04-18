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