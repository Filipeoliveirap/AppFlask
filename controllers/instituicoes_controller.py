from flask import Blueprint, request, jsonify
from services.instituicoes_service import InstituicaoService
from models.InstituicaoEnsino import InstituicaoEnsino

instituicoes_bp = Blueprint("instituicoes", __name__, url_prefix="/instituicoes")

service = InstituicaoService()

@instituicoes_bp.route("/", methods=["GET"])
def listar_instituicoes():
    try:
        data = service.listar_todas()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@instituicoes_bp.route("/instituicoes", methods=["POST"])
def create_instituicao():
    try:
        data = request.get_json()
        nova_ie = service.create_instituicao(InstituicaoEnsino(**data))
        return jsonify(nova_ie.__dict__), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@instituicoes_bp.route("/instituicoes/<id>", methods=["PUT"])
def update_instituicao(id):
    try:
        novos_dados = request.get_json()
        ie_atualizada = service.update_instituicao(id, novos_dados)
        if ie_atualizada:
            return jsonify(ie_atualizada.__dict__), 200
        return jsonify({"error": "Instituição não encontrada"}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@instituicoes_bp.route("/instituicoes/<id>", methods=["DELETE"])
def delete_instituicao(id):
    try:
        sucesso = service.delete_instituicao(id)
        if sucesso:
            return jsonify({"message": "Instituição deletada"}), 200
        return jsonify({"error": "Instituição não encontrada"}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 500


@instituicoes_bp.route("/<int:id_instituicao>", methods=["GET"])
def buscar_instituicao(id_instituicao):
    try:
        resultado, status = service.buscar_instituicao_por_id(id_instituicao)
        return jsonify(resultado), status
    except Exception as e:
        return jsonify({"erro": str(e)}), 500
