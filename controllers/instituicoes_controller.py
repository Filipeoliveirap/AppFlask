from flask import Blueprint, request, jsonify
import services.instituicoes_service as instituicoes_service

instituicoes_bp = Blueprint("instituicoes", __name__)

@instituicoes_bp.route("/instituicoes", methods=["GET"])
def Read_instituicoes():
    ies = instituicoes_service.list_instituicoes()
    return jsonify([ie.__dict__ for ie in ies]), 200

@instituicoes_bp.route("/instituicoes", methods=["POST"])
def Create_instituicao():
    data = request.get_json()
    nova_ie = instituicoes_service.create_instituicao(instituicoes_service.InstituicaoEnsino(**data))
    return jsonify(nova_ie.__dict__), 201

@instituicoes_bp.route("/instituicoes/<id>", methods=["PUT"])
def Update_instituicao(id):
    novos_dados = request.get_json()
    ie_atualizada = instituicoes_service.update_instituicao(id, novos_dados)
    if ie_atualizada:
        return jsonify(ie_atualizada.__dict__), 200
    return jsonify({"error": "Instituição não encontrada"}), 404

@instituicoes_bp.route("/instituicoes/<id>", methods=["DELETE"])
def delete_instituicao(id):
    sucesso = instituicoes_service.delete_instituicao(id)
    if sucesso:
        return jsonify({"message": "Instituição deletada"}), 200
    return jsonify({"error": "Instituição não encontrada"}), 404

@instituicoes_bp.route("/instituicoes/<id>", methods=["GET"])
def get_instituicao_by_id(id):
    ie = instituicoes_service.get_instituicao_by_id(id)
    if ie:
        return jsonify(ie.__dict__), 200
    return jsonify({"error": "Instituição não encontrada"}), 404