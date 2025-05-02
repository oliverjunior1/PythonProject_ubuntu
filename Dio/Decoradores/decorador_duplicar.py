def duplicar(func):
    def envelope(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    #return evelope

@duplicar
def aprender(tecnologia):
    print(f"Estou aprendendo {tecnologia}")

aprender("Python")