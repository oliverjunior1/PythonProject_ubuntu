# TODO: Crie uma Lista 'itens' para armazenar os equipamentos:
lista_de_equipamentos = []

# TODO: Crie um loop para solicitar os itens ao usuário:
i = 0
while i < 3:
    lista = input()
    # TODO: Solicite o item e armazena na variável "item":
    lista_de_equipamentos.append(lista)
    i += 1
# TODO: Adicione o item à lista "itens":
print("Lista de Equipamentos:")
for itens in lista_de_equipamentos:
    print(f"- {itens}")

# Exibe a lista de itens
# print("Lista de Equipamentos:")
