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