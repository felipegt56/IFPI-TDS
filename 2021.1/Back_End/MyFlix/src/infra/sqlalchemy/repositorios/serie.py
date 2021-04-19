from sqlalchemy.orm import Session
from src.schema import schemas
from src.infra.sqlalchemy.models import models


class RepositorioSerie():

    def __init__(self, db: Session):
        self.db = db

    def cadastrar(self, serie: schemas.Serie):
        db_serie = models.Serie(titulo=serie.titulo,
                                    ano=serie.ano,
                                    genero=serie.genero,
                                    qtd_temporadas=serie.qtd_temporadas)
        self.db.add(db_serie)
        self.db.commit()
        self.db.refresh(db_serie)
        return db_serie

    def listar(self):
        serie = self.db.query(models.Serie).all()
        return serie


   