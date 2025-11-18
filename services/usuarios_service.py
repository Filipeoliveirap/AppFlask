from repository.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self):
        self.repository = UsuarioRepository()

    def listar_todos(self):
        return self.repository.find_all(), 200

    def buscar_por_id(self, id_usuario: int):
        usuario = self.repository.find_by_id(id_usuario)
        if not usuario:
            return {"erro": "Usuário não encontrado"}, 404
        return usuario, 200

    def criar(self, dados: dict):
        new_id = self.repository.create(dados)
        if not new_id:
            return {"erro": "Erro ao criar usuário"}, 500

        dados["id"] = new_id
        return dados, 201

    def atualizar(self, id_usuario: int, dados: dict):
        sucesso = self.repository.update(id_usuario, dados)
        if not sucesso:
            return {"erro": "Usuário não encontrado"}, 404
        return dados, 200

    def deletar(self, id_usuario: int):
        sucesso = self.repository.delete(id_usuario)
        if not sucesso:
            return {"erro": "Usuário não encontrado"}, 404
        return {"mensagem": "Usuário removido"}, 200
