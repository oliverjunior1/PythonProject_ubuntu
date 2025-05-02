def meu_decorador(funcao):
    def envelope():
        print("faz algo antes de executar")
        funcao()
        print("Faz algo depois de executar")
    return envelope()

@meu_decorador
def ola_mundo(nome):
    print(f"Olá mundo {nome}!")

ola_mundo()