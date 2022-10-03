from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from typing import List


import atividade
import professor

app = FastAPI()

class CreateAtividadeRequest(BaseModel):
    nome: str
    nota: float


@app.get("/")
async def root():
    return {"status": "ok"}

@app.get("/test")
async def test():
    return {"testando 123"}

@app.post("/atividade",response_model= atividade.Atividade)
async def create_atividade(aluno_req: CreateAtividadeRequest):
    atividade = atividade.create_atividade(aluno_req.dict())
    professor.emit_atividade_enviada(atividade)

    return atividade

#@app.post("/atividade", response_model= atividade.Atividade)
#async def create_order(aluno_req: CreateAlunoRequest):

