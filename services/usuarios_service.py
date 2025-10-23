from models.Usuario import Usuario
from helpers.data.file_helper import read_json, write_json
import os

USUARIOS_FILE = os.path.join("data", "usuarios.json")

def _read_usuarios():
    data = read_json(USUARIOS_FILE)
    return [Usuario(**u) for u in data]

def _write_usuarios(usuarios):
    data = [u.__dict__ for u in usuarios]
    write_json(USUARIOS_FILE, data)

# CRUD completo

def list_usuarios():
    return _read_usuarios()

def create_usuario(novo_usuario: Usuario):
    usuarios = _read_usuarios()
    usuarios.append(novo_usuario)
    _write_usuarios(usuarios)
    return novo_usuario

def update_usuario(usuario_id, novos_dados: dict):
    usuarios = _read_usuarios()
    atualizado = None
    for u in usuarios:
        if u.id == usuario_id:
            for k, v in novos_dados.items():
                setattr(u, k, v)
            atualizado = u
    if atualizado:
        _write_usuarios(usuarios)
    return atualizado

def delete_usuario(usuario_id):
    usuarios = _read_usuarios()
    nova_lista = [u for u in usuarios if u.id != usuario_id]
    if len(nova_lista) < len(usuarios):
        _write_usuarios(nova_lista)
        return True
    return False

def get_usuario_by_id(usuario_id):
    usuarios = _read_usuarios()
    return next((u for u in usuarios if u.id == usuario_id), None)

