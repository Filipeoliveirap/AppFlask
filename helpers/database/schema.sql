CREATE TABLE IF NOT EXISTS tb_instituicao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    codigo TEXT NOT NULL,
    nome TEXT NOT NULL,
    co_uf INTEGER,
    co_municipio INTEGER,
    qt_mat_bas INTEGER,
    qt_mat_inf INTEGER,
    qt_mat_fund INTEGER,
    qt_mat_med INTEGER,
    qt_mat_prof INTEGER,
    qt_mat_esp INTEGER
);


CREATE TABLE IF NOT EXISTS tb_usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        cpf TEXT NOT NULL,
        nascimento DATE NOT NULL
);