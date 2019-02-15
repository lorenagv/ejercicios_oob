class Contador():
    def __init__(self, numero):
        self.numero = numero
    def suma_uno(self):
        return self.numero + 1
    def resta_uno(self):
        return self.numero - 1

c = Contador(1)
print(c.suma_uno())
