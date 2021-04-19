from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schema.schemas import Serie
from src.infra.sqlalchemy.config.database import get_db, criar_bd
from src.infra.sqlalchemy.repositorios.serie import RepositorioSerie

criar_bd()

app = FastAPI()


@app.post('/series')
def cadastra_series(serie: Serie, db: Session = Depends(get_db)):
    serie_cadastrada = RepositorioSerie(db).cadastrar(serie)
    return serie_cadastrada


@app.get('/series')
def listar_series(db: Session = Depends(get_db)):
    serie = RepositorioSerie(db).listar()
    return serie

