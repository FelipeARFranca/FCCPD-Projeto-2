CREATE TABLE IF NOT EXISTS mensagens (
    id SERIAL PRIMARY KEY,
    conteudo TEXT NOT NULL,
    criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


INSERT INTO mensagens (conteudo) VALUES ('Registro inicial do desafio 2');