def meu_decoarador(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar")
        funcao(*args, **kwargs)
        print("Faz algo depois de executar")
    return envelope

@meu_decoarador
def ola_mundo(nome, outro_argumento):
    print(f"Olá mundo {nome}!")

ola_mundo("Joao", 1000)