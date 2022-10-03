from enum import Enum
from typing import List

from uuid import UUID, uuid4
import uuid

from pydantic import BaseModel



ATIVIDADE = {}

class AtividadeStatus(str, Enum):
    feita = 'feita'
    entregue = 'entregue'
    corrigida = 'corrigida'
    nao_corrigida= 'não corrigida'

class Atividade(BaseModel):
    atividade_id : UUID
    nome: str
    nota: float

def create_atividade(nome: str,nota: float):
   
    atividade = Atividade(
        atividade_id=uuid4(),
        nome = nome,
        nota = nota,
    )
    ATIVIDADE[str(atividade.atividade_id)] = atividade
    
    return atividade

