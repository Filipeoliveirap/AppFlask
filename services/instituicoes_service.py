from helpers.data import getInstituicoesEnsino
from models.InstituicaoEnsino import InstituicaoEnsino
import json
import os
import uuid

DATA_FILE = os.path.join("data", "instituicoes_pb.json")

def write_instituicoes(instituicoes):
    data = [ie.to_json() for ie in instituicoes] 
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def list_instituicoes():
    return getInstituicoesEnsino()

def create_instituicao(nova_ie: InstituicaoEnsino):
    ies = getInstituicoesEnsino()
    
    if not hasattr(nova_ie, "id") or nova_ie.id is None:
        nova_ie.id = str(uuid.uuid4())
    
    ies.append(nova_ie)
    write_instituicoes(ies)
    return nova_ie

def update_instituicao(id, novos_dados: dict):
    ies = getInstituicoesEnsino()
    atualizada = None

    for ie in ies:
        if getattr(ie, "id", None) == str(id):
            for k, v in novos_dados.items():
                setattr(ie, k, v)
            atualizada = ie
            break
    
    if atualizada:
        write_instituicoes(ies)
    return atualizada

def delete_instituicao(id):
    ies = getInstituicoesEnsino()
    new_list = [ie for ie in ies if getattr(ie, "id", None) != str(id)]
    
    if len(new_list) < len(ies):
        write_instituicoes(new_list)
        return True
    return False

def get_instituicao_by_id(id):
    ies = getInstituicoesEnsino()
    return next((ie for ie in ies if getattr(ie, "id", None) == str(id)), None)
