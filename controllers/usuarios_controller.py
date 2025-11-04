from flask import Blueprint, request, jsonify
import services.usuarios_service as usuarios_service
from models.Usuario import Usuario

usuarios_bp = Blueprint("usuarios", __name__)

@usuarios_bp.route("/usuarios", methods=["GET"])
def read_usuarios():
    usuarios = usuarios_service.list_usuarios()
    return jsonify([u.__dict__ for u in usuarios]), 200

@usuarios_bp.route("/usuarios", methods=["POST"])
def create_usuario():
    data = request.get_json()
    novo_usuario = Usuario(**data)
    usuario_criado = usuarios_service.create_usuario(novo_usuario)
    return jsonify(usuario_criado.__dict__), 201

@usuarios_bp.route("/usuarios/<int:usuario_id>", methods=["PUT"])
def update_usuario(usuario_id):
    novos_dados = request.get_json()
    usuario_atualizado = usuarios_service.update_usuario(usuario_id, novos_dados)
    if usuario_atualizado:
        return jsonify(usuario_atualizado.__dict__), 200
    return jsonify({"error": "Usuário não encontrado"}), 404

@usuarios_bp.route("/usuarios/<int:usuario_id>", methods=["DELETE"])
def delete_usuario(usuario_id):
    sucesso = usuarios_service.delete_usuario(usuario_id)
    if sucesso:
        return jsonify({"message": "Usuário deletado"}), 200
    return jsonify({"error": "Usuário não encontrado"}), 404

@usuarios_bp.route("/usuarios/<int:usuario_id>", methods=["GET"])
def get_user_by_id(usuario_id):
    usuario = usuarios_service.get_usuario_by_id(usuario_id)
    if usuario:
        return jsonify(usuario.__dict__), 200
    return jsonify({"error": "Usuário não encontrado"}), 404
