
class Usuario:
    
    def __init__(self, id, nome, idade):
        self.id = id
        self.nome = nome
        self.idade = idade

usuario = Usuario(1, "Ricardo", 37) # argumento posicional
usuario = Usuario(id=1, nome="Ricardo", idade=30) # argumentos nomeado com campos
usuario_2 = Usuario(id=2, nome="Fabio", idade=24)
print(usuario.id, usuario.nome, usuario.idade)
print(usuario_2.id, usuario_2.nome, usuario_2.idade)