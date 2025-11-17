Desafio 4 — Microsserviços Independentes
Objetivo:
    Criar dois microsserviços independentes que se comunicam via HTTP.

Descrição da Solução:
    Duas imagens/containers são criadas: service-a e service-b. O service-a responde em /users com uma lista JSON de usuários. O service-b faz uma requisição HTTP para o service-a e processa a resposta exibindo a lista de usuários. Dentro desse contexto, o service-b consome informações fornecidas pelo service-a.

    Cada serviço possui seu próprio Dockerfile e roda separadamente. Como já mencionado, a comunicação é feita diretamente via HTTP, não há API Gateway, apenas DNS interno do docker compose.

Arquitetura:

    +------------------------+                         +------------------------+
    |       service-a        |     HTTP GET /users     |       service-b        |
    |     (User Service)     +------------------------>|   (Consumer Service)   |
    |   Porta interna: 5000  |                         |   Porta interna: 5001  |
    +------------------------+                         +-----------+------------+
                                                                   |
                                                          Resposta formatada
                                                                   |
                                                          Exposta ao host em
                                                          http://localhost:5001

Instruções de Execução:

    Passo 1:
        No diretório /desafio4 rode: docker compose up --build

    Passo 2:
        Para testar o service-a, acesse: http://localhost:5000/users

        A página deve exibir a seguinte saída:
        [
            {
                "ativo_desde": "2021-01-10",
                "id": 1,
                "nome": "Alice"
            },
            {
                "ativo_desde": "2022-03-05",
                "id": 2,
                "nome": "Bruno"
            }
        ]

        Para testar o service-b, acesse: http://localhost:5001

        A página deve exibir a seguinte saída:

        Usuário Alice — ativo desde 2021-01-10
        Usuário Bruno — ativo desde 2022-03-05

    Passo 3:
        Para acessar os logs dos serviços, rode no terminal: docker compose logs -f

        Ao acessar os logs, será possível visualizar o service-b fazendo requisições ao service-a e este as respondendo.
