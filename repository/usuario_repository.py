import sqlite3
import os

class UsuarioRepository:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.database_path = os.path.join(base_dir, "..", "..", "censoescolar.db")

    def find_all(self):
        try:
            conn = sqlite3.connect(self.database_path)
            cursor = conn.cursor()
            cursor.execute("SELECT id, nome, cpf, nascimento FROM tb_usuario")

            colunas = [col[0] for col in cursor.description]
            usuarios = [dict(zip(colunas, row)) for row in cursor.fetchall()]

            conn.close()
            return usuarios
        except Exception as e:
            print(f"Erro ao buscar usuários: {e}")
            return []

    def find_by_id(self, id_usuario: int):
        try:
            conn = sqlite3.connect(self.database_path)
            cursor = conn.cursor()

            cursor.execute("""SELECT id, nome, cpf, nascimento
                              FROM tb_usuario WHERE id = ?""",
                           (id_usuario,))
            row = cursor.fetchone()
            conn.close()

            if row:
                colunas = ["id", "nome", "cpf", "nascimento"]
                return dict(zip(colunas, row))
            return None
        except Exception as e:
            print(f"Erro ao buscar usuário por id: {e}")
            return None

    def create(self, data: dict):
        try:
            conn = sqlite3.connect(self.database_path)
            cursor = conn.cursor()

            cursor.execute("""
                INSERT INTO tb_usuario (nome, cpf, nascimento)
                VALUES (?, ?, ?)
            """, (data["nome"], data["cpf"], data["nascimento"]))

            conn.commit()
            new_id = cursor.lastrowid
            conn.close()
            return new_id
        except Exception as e:
            print(f"Erro ao criar usuário: {e}")
            return None

    def update(self, id_usuario: int, data: dict):
        try:
            conn = sqlite3.connect(self.database_path)
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE tb_usuario SET nome=?, cpf=?, nascimento=?
                WHERE id = ?
            """, (data["nome"], data["cpf"], data["nascimento"], id_usuario))

            conn.commit()
            updated = cursor.rowcount > 0
            conn.close()
            return updated
        except Exception as e:
            print(f"Erro ao atualizar usuário: {e}")
            return False

    def delete(self, id_usuario: int):
        try:
            conn = sqlite3.connect(self.database_path)
            cursor = conn.cursor()

            cursor.execute("DELETE FROM tb_usuario WHERE id = ?", (id_usuario,))
            conn.commit()
            deleted = cursor.rowcount > 0
            conn.close()
            return deleted
        except Exception as e:
            print(f"Erro ao deletar usuário: {e}")
            return False
