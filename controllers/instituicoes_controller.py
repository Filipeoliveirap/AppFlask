from flask import Blueprint, request, jsonify
from services.instituicoes_service import InstituicaoService

instituicoes_bp = Blueprint("instituicoes", __name__, url_prefix="/instituicoes")
service = InstituicaoService()

@instituicoes_bp.get("/")
def listar():
    data = service.listar_todas()
    return jsonify(data), 200

@instituicoes_bp.post("/")
def criar():
    dados = request.get_json()
    data, status = service.criar(dados)
    return jsonify(data), status

@instituicoes_bp.get("/<int:id_instituicao>")
def buscar(id_instituicao):
    data, status = service.buscar_instituicao_por_id(id_instituicao)
    return jsonify(data), status

@instituicoes_bp.put("/<int:id_instituicao>")
def atualizar(id_instituicao):
    dados = request.get_json()
    data, status = service.atualizar(id_instituicao, dados)
    return jsonify(data), status

@instituicoes_bp.delete("/<int:id_instituicao>")
def deletar(id_instituicao):
    data, status = service.deletar(id_instituicao)
    return jsonify(data), status
