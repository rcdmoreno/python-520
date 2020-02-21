def sexta():
    pass

def quinta():
    return 8 / 0

def quarta():
    quinta()

def terceira():
    sexta()

def segunda():
    quarta()

def primeira():
    segunda()
    try:
        terceira()
    except:
        print('peguei o erro')

primeira()