lista = [ 0 ]
dicionario = { 'nome': 'Lucas' }

def emite_erro(numero):
    if numero == 1:
        lista[1]                # IndexError
    elif numero == 2:
        dicionario['email']     # KeyError
    elif numero == 3:
        8 / 0                   # ZeroDivisionError

def primeira():
    for i in range(1, 4):
        try:
            emite_erro(i)
        except IndexError:
            print('Esse foi um IndexError')
        except KeyError:
            print('Esse foi um KeyError')
        except ZeroDivisionError:
            print('Esse foi um ZeroDivisionError')
        except Exception:
            print('capturei o erro generico')
        
primeira()