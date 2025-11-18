import sqlite3
import os

class InstituicaoRepository:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.database_path = os.path.join(base_dir, "..", "..", "censoescolar.db")

    def connect(self):
        return sqlite3.connect(self.database_path)

    def find_all(self):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            query = """
                SELECT codigo, nome, co_uf, co_municipio,
                       qt_mat_bas, qt_mat_inf, qt_mat_fund,
                       qt_mat_med, qt_mat_prof, qt_mat_esp
                FROM tb_instituicao
            """
            cursor.execute(query)

            colunas = [c[0] for c in cursor.description]
            instituicoes = [dict(zip(colunas, row)) for row in cursor.fetchall()]

            conn.close()
            return instituicoes
        except Exception as e:
            print(f"Falha ao buscar instituições: {e}")
            return []

    def buscar_por_id(self, id_instituicao: int):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            query = """
                SELECT codigo, nome, co_uf, co_municipio,
                       qt_mat_bas, qt_mat_inf, qt_mat_fund,
                       qt_mat_med, qt_mat_prof, qt_mat_esp
                FROM tb_instituicao
                WHERE codigo = ?
            """
            cursor.execute(query, (id_instituicao,))
            row = cursor.fetchone()
            conn.close()

            if row:
                colunas = ["codigo", "nome", "co_uf", "co_municipio",
                           "qt_mat_bas", "qt_mat_inf", "qt_mat_fund",
                           "qt_mat_med", "qt_mat_prof", "qt_mat_esp"]
                return dict(zip(colunas, row))
            return None
        except sqlite3.Error as e:
            print(f"Erro ao buscar instituição por id: {e}")
            return None

    def create(self, data: dict):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO tb_instituicao (
                    codigo, nome, co_uf, co_municipio,
                    qt_mat_bas, qt_mat_inf, qt_mat_fund,
                    qt_mat_med, qt_mat_prof, qt_mat_esp
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, tuple(data.values()))
            conn.commit()
            conn.close()
            return True
        except Exception as e:
            print(f"Erro ao inserir instituição: {e}")
            return False

    def update(self, id_instituicao: int, data: dict):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE tb_instituicao SET
                    nome=?, co_uf=?, co_municipio=?,
                    qt_mat_bas=?, qt_mat_inf=?, qt_mat_fund=?,
                    qt_mat_med=?, qt_mat_prof=?, qt_mat_esp=?
                WHERE codigo = ?
            """, (
                data["nome"], data["co_uf"], data["co_municipio"],
                data["qt_mat_bas"], data["qt_mat_inf"], data["qt_mat_fund"],
                data["qt_mat_med"], data["qt_mat_prof"], data["qt_mat_esp"],
                id_instituicao
            ))
            conn.commit()
            conn.close()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Erro ao atualizar instituição: {e}")
            return False

    def delete(self, id_instituicao: int):
        try:
            conn = self.connect()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM tb_instituicao WHERE codigo = ?", (id_instituicao,))
            conn.commit()
            conn.close()
            return cursor.rowcount > 0
        except Exception as e:
            print(f"Erro ao deletar instituição: {e}")
            return False
