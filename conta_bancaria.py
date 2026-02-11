class ContaBancaria:

    def __init__(self, cliente, conta, saldo, limite_saque):
        self.cliente = cliente
        self.conta = conta
        self.saldo = saldo
        self.extrato = []
        self.limite_saque = limite_saque


    def depositar(self, valor_deposito):
        self.valor_deposito = valor_deposito
        
        if valor_deposito <= 0:
            print("O valor para depósito deve ser maior do que 0")
        else:
            self.saldo += valor_deposito
            print(f"Depósito realizado com sucesso. Seu novo saldo é de R${self.saldo:.2f}")
            self.extrato.append(f"Depósito: R${valor_deposito:.2f}. Saldo após o DEPÓSITO: R${self.saldo:.2f}")

    def sacar(self, valor_saque):
        self.valor_saque = valor_saque
        
        if self.limite_saque >= 3:
            print("Seu limite de saques diários foi excedido. Tente novamente outro dia")

        elif valor_saque > 500:
            print("Seu limite diário para saque é de R$ 500,00")

        elif self.saldo < valor_saque:
            print(f"Saldo insuficiente! Saldo atual de R${self.saldo:.2f}")
            
        else:
            self.saldo -= valor_saque
            print(f"Saque no valor de R${valor_saque:.2f} realizado com sucesso.\nSeu novo saldo é de R${self.saldo:.2f}")
            self.extrato.append(f"Saque: R${valor_saque:.2f}. Saldo após o SAQUE: R${self.saldo:.2f}")
            self.limite_saque += 1

    def extrato_bancario(self):
        
        
        if not self.extrato:            
            print("Não foram realizadas movimentações")
        else:

            print(self.extrato)
            print(f"Seu saldo atual é de R${self.saldo:.2f}")
        

cliente = ContaBancaria("Aramyz", 1, 0, 0)
cliente.depositar(400)
cliente.sacar(20)
cliente.sacar(10)
cliente.sacar(10)
cliente.sacar(10)

# cliente.extrato_bancario()

