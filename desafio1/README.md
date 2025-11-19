Desafio 1 — Containers em Rede
Objetivo:
    Criar dois containers que se comunicam por uma rede Docker customizada.

Descrição da Solução:
    Duas imagens/containers são criadas: web-server e requester. O web-server é um servidor HTTP simples (Flask) executando na porta 8080 dentro do container. Ele fornece uma rota / que responde com um JSON contendo a mensagem e timestamp. O requester executa um loop em shell usando curl para pedir periodicamente a rota do web-server e logar a resposta.

    Os containers são conectados em uma rede docker nomeada rede_desafio1 (modo bridge). A comunicação é feita usando o nome do container.

Arquitetura:

    +----------------+          bridge network (rede_desafio1)           +----------------+
    |                |          <--HTTP--> (DNS: web-server)             |                |
    | requester      | <-----------------------------------------------> | web-server     |
    | (curl loop)    |                                                   | (Flask 8080)   |
    +----------------+                                                   +----------------+

    Fluxo de funcionamento: 
        -> requester faz curl http://web-server:8080/ a cada N segundos 
        -> web-server recebe a requisição e responde com JSON (mensagem + timestamp) 
        -> requester imprime a resposta no stdout

Instruções de Execução:

    Passo 1:
        No diretório /desafio1 rode: docker compose up --build
    
    Passo 2:
        Para visualizar o sistema funcionando pode se verificar o log stdout no próprio terminal, abrir terminais separados para cada um dos containters com:
            docker logs -f requester
            docker logs -f web-server
        ou pelo app docker desktop

        Espera-se que os logs mostrem o output do requester, requisições e respostas JSON do web-server seguindo o seguinte formato:

        [requester] 2025-11-16T18:12:12Z -> requesting http://web-server:8080/⁠
        {"message":"Hello from web-server","timestamp":"2025-11-16T18:12:12.709681Z"}

        
        Além disso, também espera-se um output do web-server no seguinte formato:

        172.18.0.3 - - [16/Nov/2025 18:12:18] "GET / HTTP/1.1" 200 -

        Isso demonstra a comunicação correta entre os containers.
