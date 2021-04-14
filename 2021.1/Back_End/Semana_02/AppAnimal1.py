from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from uuid import uuid4


app = FastAPI()

class Animais(BaseModel):
    id: Optional[str]
    nome: str
    idade: int
    sexo: str
    cor: str


bd_animais: List[Animais] = []



@app.post('/animais')
def Sistema_cadastro(animal: Animais):
    animal.id = str(uuid4())
    bd_animais.append(animal)
    return None


@app.get('/animais')
def listar_animais():
    return bd_animais

@app.get('/animais/{animal_id}')
def localizar_id(animal_id: str):
    for animal in bd_animais:
        if animal.id ==  animal_id:
            return animal
        
    return {'erro': 'Animal não encontrado'}


@app.delete('/animais/{animal_id}')
def deleta_id(animal_id: str):
    pos = -1
    for index, animal in enumerate(bd_animais):
        if animal.id == animal_id:
            pos = index
            break
    if pos != -1:
        bd_animais.pop(pos)
        return {'Mensagem': 'animal removido com sucesso!'}
    else:
        return {'Erro': 'Animal não encontrado!'}