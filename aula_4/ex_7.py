import json


usuario = {
    'nome': 'Lucas',
    'email': 'lucas@email',
    'senha': 'admin'
}

# Salvar um arquivo JSON
with open('usuario.json', 'w') as f:
    f.write(json.dumps(usuario, indent=2))

# Ler um arquivo JSON
with open('usuario.json', 'r') as f:
    usuario = json.loads(
        ''.join(l for l in f.readlines())
    )
    print(usuario)