# Tem que ter saldo maior que 4.40
# Tem que pertencer a sptrans

catraca_liberada = False
meu_saldo = 2.0
concessionaria_cartao = 'sptrans'

class SaldoInsuficienteError(Exception):
    pass

class ConcessionariaDiferenteError(Exception):
    pass

try:

    if meu_saldo < 4.40:
        raise SaldoInsuficienteError(meu_saldo)
    
    if concessionaria_cartao != 'sptrans':
        raise ConcessionariaDiferenteError()

    meu_saldo = meu_saldo - 4.40
    catraca_liberada = True

    print('Tudo ocorreu bem :)')

except SaldoInsuficienteError as err:
    print('Saldo insuficiente: ' + str(err))

except ConcessionariaDiferenteError:
    print('Concessionária diferente')

except:
    print('Erro genérico')