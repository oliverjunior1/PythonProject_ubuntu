# from abc import ABC, abstractmethod, abstractproperty
# from datetime import datetime
#
# from Dio.a_desafio import excedeu_saldo, numero_saques
#
#
# class Cliente:
#     def __init__(self,endereco):
#         self.endereco = endereco
#         self.contas = []
#
#     def realizar_transacao(self, conta, transacao):
#         transacao.registrar(conta)
#
#     def adicionar_conta(self, conta):
#         self.contas.append(conta)
#
# class PessoaFisica(Cliente):
#     def __init__(self, nome, data_nascimento, cpf, endereco):
#         super().__init__(endereco)
#         self.nome = nome
#         self.data_nascimento = data_nascimento
#         self.cpf = cpf
#
# class Conta:
#     def __init__(self, numero, cliente):
#         self._saldo = 0
#         self._numero = numero
#         self._agencia = "001"
#         self._historico = Historico()
#
#     @classmethod
#     def nova_conta(cls, cliente, numero):
#         return cls(numero, cliente)
#
#     @@property
#     def saldo(self):
#         return self._saldo
#
#     @property
#     def numero(self):
#         return self._numero
#
#     @property
#     def agencia(self):
#         return = self._agencia
#
#     @property
#     def cliente(self):
#         return self._cliente
#
#     @property
#     def historico(self):
#         return self._historico
#
#     @property
#     def sacar(self, valor):
#         saldo = self.saldo
#         excedeu_saldo = valor > saldo
#
#         if excedeu_saldo:
#             print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
#
#         elif valor > 0:
#             self.saldo -= valor
#             print("\n=== Saque realizado com sucesso!===")
#             return True
#
#         else:
#             print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
#         return False
#
#     def depositar(self, valor):
#         if valor > 0:
#             self._saldo += valor
#             print("\n=== Depósito realizado com sucesso!===")
#         else:
#             print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
#             return False
#         return TrueC
#
# class ContaCorrente(Conta):
#     def __init__(self, numero, cliente, limite=500, limite_saques=3):
#         super().__init__(numero, cliente)
#         self.limite = limite
#         self.limite_saques = limite_saques
#
#     def sacar(self, valor):
#         numero_saques = len(
#             [transacao for transcao in self.historico.transacoes if transacao['tipo']==Saque.__name__]
#         )
#
#         excedeu_limite = valor > self.limite
#         excedeu_saques = numero_saues > self.limite_saques
#
#         if excedeu_limite:
#             print("\n@@@ Operação falhou! O valor do saque excede o Limite. @@@")
#
#         elif excedeu_saques:
#             print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
#
#         else:
#             return super().sacar(valor)
#
#         return False
#
#     def __str__(self):
#         return f"""
#         Agência:\t{self.agencia}
#         C/C:\t{self.numero}
#         Titular:\t{self.cliente.nome}
# """
#
#         return False
#
# class Historico:
#     def __init__(self):
#         self._transacoes = []
#
#     @property
#     def transacoes(self):
#         return self._transacoes
#
#     def adicionar_transacao(self, transacao):
#         self._transacoes.append(
#             {
#                 "tipo":transacao.__class__.__name__,
#             }
#         )

