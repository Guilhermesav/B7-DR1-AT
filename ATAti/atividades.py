from enum import Enum
from locale import strcoll
from typing import List

from uuid import UUID, uuid4


from pydantic import BaseModel



ATIVIDADE = {}

class AtividadeStatus(str, Enum):
    feita = 'feita'
    entregue = 'entregue'
    aprovada = 'aprovada'
    reprovada= 'reprovada'

class Atividade(BaseModel):
    atividade_id : UUID
    nome: str
    aluno: str
    nota: float
    disciplina: str
    status: AtividadeStatus = AtividadeStatus.entregue

def create_atividade(nome: str,aluno:str,disciplina:str):
   
    atividade = Atividade(
        atividade_id=uuid4(),
        nome = nome,
        nota = 0,
        aluno = aluno,
        disciplina= disciplina
    )
    ATIVIDADE[str(atividade.atividade_id)] = atividade
    
    return atividade

def get_atividades():

    atividades = ATIVIDADE
    return atividades


def get_atividade(atividade_id: str):
    return ATIVIDADE.get(atividade_id)
