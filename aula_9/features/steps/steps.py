
import behave


def soma(x, y):
    return x + y

@behave.step('somar "{num1}" com "{num2}"')
def test_soma(context, num1, num2):
    context.r_soma = soma(int(num1), int(num2))

@behave.step('o resultado deve ser "{esperado}"')
def test_soma_result(context, esperado):
    assert context.r_soma == int(esperado), "descrição do erro"

## exdcucao no terminal : behave features/funcionalidades.feature