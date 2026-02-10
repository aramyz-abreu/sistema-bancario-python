# Projeto simples de um funcionamento de aplicativo bancário
O projeto foi proposto pelo professor Guilherme Arthur de Carvalho, no curso "Santander 2025 - Back-End com Python" da DIO.

# Qual contexto do desafio?
Fomos contratados po um grande banco para desenvolver seu sistema. Esse banco deseja modernizar suas operações e para isso escolheu a linguagem Python. Para a primeira versão do sistema devemos implementar 3 operações: depósito, saque e extrato

# Requisitos da Operação de depósito
Deve ser possível depositar valores positivos para minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato

# Requisitos da Operação de Saque
O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500.00 por saque. Caso o usuário não tenha saldo em conta, o s istema deve exibir a mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato

# Requisitos da operação de extrato
Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realziadas movimentações.
Os valores devem ser exibidos utilizando o formato R$ XXX.XX, exemplo:
1500.45 = R$ 1500.45