# decorations without method
def oliveira(text):
    def fun():
        print("Oliveira Ltda")
        print("###############")
        text()
        print("################")
        print("Contato: 99 9999 9999")
        print("Thank you for all!!!")
        print()
    return fun

@oliveira
def x():
    print("How are you?")

@oliveira
def y():
    print("Jesus loves you!")

x()
y()