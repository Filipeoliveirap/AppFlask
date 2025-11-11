from helpers.data import getInstituicoesEnsino
from models.InstituicaoEnsino import InstituicaoEnsino
import json
import os
import uuid

from repository.instituicao_repository import InstituicaoRepository

DATA_FILE = os.path.join("data", "instituicoes_pb.json")
class InstituicaoService:
    def __init__(self):
        self.repository = InstituicaoRepository()
    
    def write_instituicoes(instituicoes):
        data = [ie.to_json() for ie in instituicoes] 
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    def listar_todas(self):
       
        instituicoes = self.repository.find_all()

        instituicoes.sort(key=lambda x: x["nome"])

        return instituicoes

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

    def buscar_instituicao_por_id(self, id_instituicao: int):
        instituicao = self.repository.buscar_por_id(id_instituicao)

        if instituicao is None:
            return {"mensagem": "Instituição não encontrada."}, 404
        
        return instituicao, 200
