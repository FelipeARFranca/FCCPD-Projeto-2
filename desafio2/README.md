Desafio 2 — Volumes e Persistência
Objetivo: 
    Demonstrar como dados persistem mesmo após a remoção de containers, utilizando volumes Docker.

Descrição da Solução:
    Duas imagens/containers são criadas: db-server e db-client. O db-server é um container executando PostgreSQL, com seus dados armazenados em um volume docker de nome pgdata_desafio2. O db-client é um container separado que acessa o banco de dados para ler dados e mostrar a persistência após a recriação do db-server.

    A persistência é demonstrada subindo o banco de dados e inserindo dados em uma tabela. Após isso, o container de banco de dados é derrubado. Em seguida, o container do banco de dados será subido novamente e então será verificado se os dados inseridos ainda permanecem lá.

Arquitetura:
    +----------------------+         Volume Docker            +----------------------+
    |                      | pgdata_desafio2 (host disk)      |                      |
    | db-server            | <------------------------------> | Sistema Host         |
    | (PostgreSQL 15)      |                                  | (Armazena arquivos)  |
    +----------------------+                                  +----------------------+
                ^
                |
                | conexão direta
                |
    +----------------------+
    | db-client            |
    | (script ou psql)     |
    +----------------------+

Instruções de Execução:

    Passo 1:
        No diretório desafio2 rode: docker compose up --build

        Acesse o banco de dados para ver se o dado inicial foi inserido:
            No terminal, rode: docker exec -it db-server psql -U admin -d desafio2
            No terminal do psql, rode: SELECT * FROM mensagens;

        Espera-se a seguinte saída:

             id |           conteudo            |         criado_em
            ----+-------------------------------+----------------------------
              1 | Registro inicial do desafio 2 | 2025-XX-XX XX:XX:XX
    
    Passo 2:

        Derrube o container com: docker compose down

        Verifique que o volume ainda existe: 
            No terminal, rode: docker volume ls
        
    Passo 3:
        Suba o container novamente: 
            No terminal, rode: docker compose up
    
    Passo 4:
        Verifique a se os dados foram persistidos:
            No terminal, rode: docker compose run db-client

            ou

            No terminal, rode: docker exec -it db-server psql -U admin -d desafio2
            No terminal do psql, rode: SELECT * FROM mensagens;
        
        Espera-se a seguinte saída:

             id |           conteudo            |         criado_em
            ----+-------------------------------+----------------------------
              1 | Registro inicial do desafio 2 | 2025-XX-XX XX:XX:XX

        Isso demonstra que a informação foi mantida mesmo após a queda do container.
