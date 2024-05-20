class Banco:
    def __init__(self):
        self.saldo = 0.0
        self.saques_diarios = []
        self.extrato = []
        self.saques_realizados_hoje = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: +R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido!")

    def sacar(self, valor):
        if self.saques_realizados_hoje >= 3:
            print("Limite de 3 saques diários atingido.")
        elif valor > 500:
            print("O limite por saque é de R$500.00.")
        elif valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            self.saldo -= valor
            self.saques_diarios.append(valor)
            self.extrato.append(f"Saque: -R${valor:.2f}")
            self.saques_realizados_hoje += 1
            print(f"Saque de R${valor:.2f} realizado com sucesso!")

    def ver_extrato(self):
        print("\nExtrato:")
        for operacao in self.extrato:
            print(operacao)
        print(f"Saldo atual: R${self.saldo:.2f}\n")

    def novo_dia(self):
        self.saques_realizados_hoje = 0
        self.saques_diarios.clear()
        print("Novo dia iniciado. Limite de saques resetado.")

def menu():
    banco = Banco()

    while True:
        print("\nBem-vindo ao Banco!")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Ver extrato")
        print("4. Novo dia")
        print("5. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            valor = float(input("Digite o valor para depósito: R$"))
            banco.depositar(valor)
        elif opcao == '2':
            valor = float(input("Digite o valor para saque: R$"))
            banco.sacar(valor)
        elif opcao == '3':
            banco.ver_extrato()
        elif opcao == '4':
            banco.novo_dia()
        elif opcao == '5':
            print("Obrigado por usar o sistema bancário!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
