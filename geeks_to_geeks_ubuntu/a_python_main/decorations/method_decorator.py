def fun1(function):
    def fun2(*args, **kwargs):
        print("First")
        function(*args, **kwargs)
        print("Second")
    return function

@fun1
def ola_mundo(nome, outro_argumento):
    print(f"Ola mundo {nome}")

resultado = ola_mundo("Joao", 1000)
print(resultado)