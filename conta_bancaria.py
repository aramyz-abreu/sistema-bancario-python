class ContaBancaria:
    limite_saque = 1
    extrato = []    

    def __init__(self, cliente, conta, saldo):
        self.cliente = cliente
        self.conta = conta
        self.saldo = saldo

    def depositar(self, valor_deposito):
        self.valor_deposito = valor_deposito
        
        if valor_deposito <= 0:
            print("O valor para depósito deve ser maior do que 0")
        else:
            self.saldo += valor_deposito
            print(f"Depósito realizado com sucesso. Seu novo saldo é de R${self.saldo:.2f}")
            ContaBancaria.extrato.append(f"Depósito: R${valor_deposito:.2f}. Novo Saldo: R${self.saldo:.2f}")

    def sacar(self, valor_saque):
        self.valor_saque = valor_saque
        
        if ContaBancaria.limite_saque > 3:
            print("Limite de saque excedido. Tente novamente outro dia")

        elif valor_saque > 500:
            print("Seu limite diário para saque é de R$ 500,00")

        elif self.saldo < valor_saque:
            print(f"Saldo insuficiente! Saldo atual de {self.saldo:.2f}")
            
        else:
            self.saldo -= valor_saque
            print(f"Saque no valor de R${valor_saque:.2f} realizado com sucesso.\nSeu novo saldo é de {self.saldo:.2f}")
            ContaBancaria.extrato.append(f"Saque: R${valor_saque:.2f}. Novo Saldo: R${self.saldo}")
            ContaBancaria.limite_saque += 1

    def extrato_bancario(self):
        
        return print(ContaBancaria.extrato)
        

cliente = ContaBancaria("Aramyz", 1, 600)
cliente.depositar(30)
cliente.sacar(350.35)

cliente.extrato_bancario()

