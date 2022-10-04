from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from typing import List


import atividades
import envioAtividade

app = FastAPI()

class CreateAtividadeRequest(BaseModel):
    nome: str
    aluno:str
    disciplina:str


@app.get("/")
async def root():
    return {"status": "ok"}

@app.get("/test")
async def test():
    return {"testando 123"}

@app.post("/atividade")
async def create_atividade(aluno_req: CreateAtividadeRequest):
    trabalho = atividades.create_atividade(**aluno_req.dict())

    envioAtividade.emit_atividade_enviada(trabalho)

    return trabalho

@app.get("/atividades")
async def get_atividades():
    listAti = atividades.get_atividades()
    
    if bool(listAti) is False:
        raise HTTPException(
            status_code=404,
            detail="Nenhuma atividade foi enviada"
        )

    return listAti

@app.get("/atividade/{atividade_id}")
async def get_atividade(atividade_id: str):
    atividade = atividades.get_atividade(atividade_id=atividade_id)

    if atividade is None:
        raise HTTPException(
            status_code=404,
            detail="atividade not found"
        )

    return atividade

class UpdateAtividadeRequest(BaseModel):
    status: atividades.AtividadeStatus
    nota: float

@app.put("/atividade/{atividade_id}")
async def update_atividade(atividade_id: str, new_atividade_req: UpdateAtividadeRequest):

    atividade = atividades.get_atividade(atividade_id = atividade_id)

    if atividade is None:
        raise HTTPException(
            status_code=404,
            detail="Atividade not found"
        )

    atividade.status = new_atividade_req.status
    atividade.nota = new_atividade_req.nota
    

    return atividade