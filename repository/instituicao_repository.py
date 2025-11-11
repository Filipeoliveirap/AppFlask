import sqlite3
import os

class InstituicaoRepository:
    def __init__(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        self.database_path = os.path.join(base_dir, "..", "..", "censoescolar.db")

    def find_all(self):
        try:
            conn = sqlite3.connect(self.database_path)
            cursor = conn.cursor()
            query = """
                SELECT codigo, nome, co_uf, co_municipio,
                       qt_mat_bas, qt_mat_inf, qt_mat_fund,
                       qt_mat_med, qt_mat_prof, qt_mat_esp
                FROM tb_instituicao
            """
            cursor.execute(query)

            colunas = [desc[0] for desc in cursor.description]
            instituicoes = [dict(zip(colunas, row)) for row in cursor.fetchall()]

            conn.close()
            return instituicoes

        except Exception as e:
            print(f"Falha ao buscar instituições: {e}")
            return []

    def buscar_por_id(self, id_instituicao: int):
        try:
            conn = sqlite3.connect(self.database_path)
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

        except sqlite3.Error as erro:
            print(f"Erro ao buscar instituição por id: {erro}")
            return None
