class ContaBancaria:
    def __init__(self, nome, numero_conta):
        self.nome = nome
        self.numero_conta = numero_conta
        self.saldo = 0.0
        self.historico_saques = []
        self.historico_depositos = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico_depositos.append(valor)
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.historico_saques.append(valor)
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saque inválido. Verifique o valor ou saldo disponível.")

    def mostrar_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

    def extrato(self):
        print("\n===== Extrato da Conta =====")
        print(f"Titular: {self.nome}")
        print(f"Número da Conta: {self.numero_conta}")
        print("\n--- Depósitos ---")
        for valor in self.historico_depositos:
            print(f"+ R${valor:.2f}")
        print("\n--- Saques ---")
        for valor in self.historico_saques:
            print(f"- R${valor:.2f}")
        self.mostrar_saldo()
        print("=============================\n")


# Exemplo de uso
nome = input("Digite o nome do titular da conta: ")
numero = input("Digite o número da conta: ")

conta = ContaBancaria(nome, numero)

while True:
    print("\nEscolha uma opção:")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Ver Extrato")
    print("4 - Sair")

    opcao = input("Opção: ")

    if opcao == '1':
        valor = float(input("Digite o valor para depósito: R$"))
        conta.depositar(valor)
    elif opcao == '2':
        valor = float(input("Digite o valor para saque: R$"))
        conta.sacar(valor)
    elif opcao == '3':
        conta.extrato()
    elif opcao == '4':
        print("Encerrando...")
        break
    else:
        print("Opção inválida. Tente novamente.")
