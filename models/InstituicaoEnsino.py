class InstituicaoEnsino:

    def __init__(self, nome, qt_mat_bas, codigo, nome_uf, municipio, mesorregiao, microrregiao, id=None):
        self.id = id
        self.nome = nome
        self.qt_mat_bas = qt_mat_bas
        self.codigo = codigo
        self.nome_uf = nome_uf
        self.municipio = municipio
        self.mesorregiao = mesorregiao
        self.microrregiao = microrregiao


    def __repr__(self):
        return f'<InstituicaoEnsino {self.id} - {self.nome}>'

    def to_json(self):
        return {
            "id": self.id,
            "nome_instituicao": self.nome,
            "quantidade_matriculas_basico": self.qt_mat_bas,
            "codigo_uf": self.codigo,
            "nome_uf": self.nome_uf,
            "municipio": self.municipio,
            "mesorregiao": self.mesorregiao,
            "microrregiao": self.microrregiao
        }
