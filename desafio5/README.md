Desafio 5 — Microsserviços com API Gateway
Objetivo:
    Criar uma arquitetura com API Gateway centralizando o acesso a dois microsserviços.

Descrição da Solução:
    Três imagens/containers são criados: user-service, order-service e gateway. O user-service fornece dados de usuários. O order-service fornece dados de pedidos. O gateway é o ponto único de entrada que encaminha requisições para os dois microsserviços.

    Um cliente poderia acessar o gateway, que faz proxy da requisição para o serviço correspondente. Os microsserviços respondem com JSON e o gateway repassa a resposta para esse cliente.

Arquitetura:
                      +-------------------------+
                      |       API Gateway       |
                      |  Endpoints:             |
                      |   - /users              |
                      |   - /orders             |
                      +-----------+-------------+
                                  |
                +-----------------+-----------------+
                |                                   |
                |                                   |
   +------------v------------+         +------------v------------+
   |    User Service         |         |     Order Service       |
   |  Endpoint: /users       |         |  Endpoint: /orders      |
   |  Porta interna: 8080    |         |  Porta interna: 7000    |
   +-------------------------+         +-------------------------+

Instruções de Execução:

    Passo 1:
        No diretório /desafio5 rode: docker compose up --build

    Passo 2:
        Para testar os serviços, acesse:
            
            Para user-service: http://localhost:8080/users

            Saída esperada:
                [
                    {
                        "id": 1,
                        "nome": "Alice"
                    },
                    {
                        "id": 2,
                        "nome": "Bruno"
                    },
                    {
                        "id": 3,
                        "nome": "Carlos"
                    }
                ]
            
            Para order-service: http://localhost:7000/orders

            Saída esperada:
                [
                    {
                        "id": 101,
                        "item": "Notebook",
                        "user_id": 1
                    },
                    {
                        "id": 102,
                        "item": "Mouse",
                        "user_id": 2
                    },
                    {
                        "id": 103,
                        "item": "Teclado",
                        "user_id": 3
                    }
                ]
    
    Passo 3:
        Para testar o gateway, acesse:

            Endpoint users: http://localhost:8000/users

            Saída esperada:
                [
                    {
                        "id": 1,
                        "nome": "Alice"
                    },
                    {
                        "id": 2,
                        "nome": "Bruno"
                    },
                    {
                        "id": 3,
                        "nome": "Carlos"
                    }
                ]

            Endpoint orders: http://localhost:8000/orders

            Saída esperada:
                [
                    {
                        "id": 101,
                        "item": "Notebook",
                        "user_id": 1
                    },
                    {
                        "id": 102,
                        "item": "Mouse",
                        "user_id": 2
                    },
                    {
                        "id": 103,
                        "item": "Teclado",
                        "user_id": 3
                    }
                ]

        É possivel notar que as informações fornecidas pelos micro-serviços estão sendo corretamente passadas ao gateway.

