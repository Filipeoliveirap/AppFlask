from repository.instituicao_repository import InstituicaoRepository

class InstituicaoService:
    def __init__(self):
        self.repository = InstituicaoRepository()

    def listar_todas(self):
        instituicoes = self.repository.find_all()
        instituicoes.sort(key=lambda x: x["nome"])
        return instituicoes

    def buscar_instituicao_por_id(self, id_instituicao: int):
        instituicao = self.repository.buscar_por_id(id_instituicao)
        if instituicao is None:
            return {"mensagem": "Instituição não encontrada."}, 404
        
        return instituicao, 200

    def criar(self, dados: dict):
        sucesso = self.repository.create(dados)
        if not sucesso:
            return {"erro": "Erro ao criar instituição"}, 500
        return dados, 201

    def atualizar(self, id_inst: int, dados: dict):
        sucesso = self.repository.update(id_inst, dados)
        if not sucesso:
            return {"erro": "Instituição não encontrada"}, 404
        return dados, 200

    def deletar(self, id_inst: int):
        sucesso = self.repository.delete(id_inst)
        if not sucesso:
            return {"erro": "Instituição não encontrada"}, 404
        return {"mensagem": "Instituição removida"}, 200
