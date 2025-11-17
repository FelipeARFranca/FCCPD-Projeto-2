Desafio 3 — Docker Compose Orquestrando Serviços 
Objetivo: 
    Usar Docker Compose para orquestrar múltiplos serviços dependentes.

Descrição da Solução:
    Três imagens/containers serão criadas: web, cache e db. O web é uma aplicação Flask simples que exibe dados armazenados no cache e no banco de dados. O cache é um serviço Redis usado como armazenamento rápido de chave-valor. O db é um banco de dados PostgreSQL usado para fazer a persistência de dados.

    A aplicação Flask acessa o Redis pelo hostname cache e o PostrgreSQL pelo hostname db. Isso se dá pelo fato de que todos os serviços estão na mesma rede interna crida pelo Docker Compose. O Flask só inicia depois que Redis e PostgreSQL forem criados (utilização do depends_on).

Arquitetura:
                                Docker Compose Network
             -----------------------------------------------------------------
            |                                                                  |
            |   +-----------+        +-----------+        +----------------+   |
            |   |           | redis  |           | sql    |                |   |
            |   |   web     +------->+   cache   +------->+      db        |   |
            |   |  (Flask)  |        |  (Redis)  |        | (PostgreSQL)   |   |
            |   +-----------+        +-----------+        +----------------+   |
            |                                                                  |
             -----------------------------------------------------------------

Instruções de Execução:
    
    Passo 1:
        No diretório desafio3 rode: docker compose up --build

        Note que, ao fazer o build da aplicação, o terminal mostra uma saída onde a aplicação web apenas sobe após db e cache já estarem de pé.

        A saída deve ser semelhante a esta:

        Attaching to cache, db, web
        db  | 
        db  | PostgreSQL Database directory appears to contain a database; Skipping initialization


        cache  | 1:C 16 Nov 2025 22:57:27.741 * oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
        db     | 




        cache  | 1:C 16 Nov 2025 22:57:27.742 * Redis version=7.4.7, bits=64, commit=00000000, modified=0, pid=1, just started
        cache  | 1:C 16 Nov 2025 22:57:27.742 # Warning: no config file specified, using the default config. In order to specify a config file use redis-server /path/to/redis.conf
        cache  | 1:M 16 Nov 2025 22:57:27.743 * monotonic clock: POSIX clock_gettime
        cache  | 1:M 16 Nov 2025 22:57:27.747 * Running mode=standalone, port=6379.
        cache  | 1:M 16 Nov 2025 22:57:27.747 * Server initialized
        cache  | 1:M 16 Nov 2025 22:57:27.749 * Loading RDB produced by version 7.4.7
        cache  | 1:M 16 Nov 2025 22:57:27.749 * RDB age 100 seconds
        cache  | 1:M 16 Nov 2025 22:57:27.749 * RDB memory usage when created 0.90 Mb
        cache  | 1:M 16 Nov 2025 22:57:27.749 * Done loading RDB, keys loaded: 1, keys expired: 0.
        cache  | 1:M 16 Nov 2025 22:57:27.749 * DB loaded from disk: 0.001 seconds
        cache  | 1:M 16 Nov 2025 22:57:27.749 * Ready to accept connections tcp
        db     | 2025-11-16 22:57:27.949 UTC [1] LOG:  starting PostgreSQL 15.14 (Debian 15.14-1.pgdg13+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 14.2.0-19) 14.2.0, 64-bit
        db     | 2025-11-16 22:57:27.950 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
        db     | 2025-11-16 22:57:27.950 UTC [1] LOG:  listening on IPv6 address "::", port 5432
        db     | 2025-11-16 22:57:27.954 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
        db     | 2025-11-16 22:57:27.961 UTC [29] LOG:  database system was shut down at 2025-11-16 22:55:47 UTC
        db     | 2025-11-16 22:57:27.981 UTC [1] LOG:  database system is ready to accept connections
        web    |  * Serving Flask app 'app'
        web    |  * Debug mode: off
        web    | WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
        web    |  * Running on all addresses (0.0.0.0)
        web    |  * Running on http://127.0.0.1:5000
        web    |  * Running on http://172.20.0.4:5000
        web    | Press CTRL+C to quit

        Isso demonstra a utilização do depends_on, fazendo com que web apenas inicie se db e cache já estiverem sido criados.
    
    Passo 2:
        Abra o navegador e acesse: http://localhost:8080/
    
        A página deve mostrar a seguinte informação:

            {
                "status": "ok",
                "visitas_cache": "3",
                "hora_db": "2025-11-16 18:32:01.123456"
            }
        
    Passo 3:
        Teste a comunicação interna com usando:

            docker exec -it cache redis-cli ping

            Testa o Redis.

            Saída esperada: PONG

            docker exec -it db psql -U admin -d desafio3 -c "SELECT NOW();"

            Testa o banco de dados.

            Saída esperada:
            
                          now
            -------------------------------
            2025-11-16 23:06:25.188318+00 
            (1 row)


