class Contador:

    def __init__(self):
        self.conta = 0
    def __del__(self):
        print("Esta ultima operacao do Python, como funcao destrutor")
    def contar(self):
        #self.conta = self.conta + 1
        self.conta += 1
    def reset(self):
        self.reset = 0


# Código cliente
contador = Contador()

for i in range(10):
    contador.contar()
print(contador.conta)
