import json
from models.InstituicaoEnsino import InstituicaoEnsino

def getInstituicoesEnsino():
    instituicoesEnsino = []

    with open('data/instituicoes_pb.json', 'r', encoding='utf-8') as f:
        instituicoesEnsinoJson = json.load(f)

    for item in instituicoesEnsinoJson:
        
        ie = InstituicaoEnsino(
            id=item.get("id"),
            nome=item.get("nome_instituicao"),
            qt_mat_bas=item.get("quantidade_matriculas_basico"),
            codigo=item.get("codigo_uf"),
            nome_uf=item.get("nome_uf"),
            municipio=item.get("municipio"),
            mesorregiao=item.get("mesorregiao"),
            microrregiao=item.get("microrregiao"),
        )
        instituicoesEnsino.append(ie)


    return instituicoesEnsino
