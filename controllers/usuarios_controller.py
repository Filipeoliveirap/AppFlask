from flask import Blueprint, request, jsonify
from services.usuarios_service import UsuarioService

usuarios_bp = Blueprint("usuarios", __name__, url_prefix="/usuarios")

service = UsuarioService()

@usuarios_bp.route("/", methods=["GET"])
def listar():
    data, status = service.listar_todos()
    return jsonify(data), status

@usuarios_bp.route("/", methods=["POST"])
def criar():
    dados = request.get_json()
    data, status = service.criar(dados)
    return jsonify(data), status

@usuarios_bp.route("/<int:id_usuario>", methods=["GET"])
def buscar(id_usuario):
    data, status = service.buscar_por_id(id_usuario)
    return jsonify(data), status

@usuarios_bp.route("/<int:id_usuario>", methods=["PUT"])
def atualizar(id_usuario):
    dados = request.get_json()
    data, status = service.atualizar(id_usuario, dados)
    return jsonify(data), status

@usuarios_bp.route("/<int:id_usuario>", methods=["DELETE"])
def deletar(id_usuario):
    data, status = service.deletar(id_usuario)
    return jsonify(data), status
