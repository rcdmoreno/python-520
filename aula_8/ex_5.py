import os
import random


class App:

    def __init__(self):
        self.lista_de_nomes = []
        self.terminado = False

    def imprimir_menu(self):
        os.system('clear')
        print('Selecione uma das opções abaixo: ')
        print('\t 1. Adicionar nome ao sorteio')
        print('\t 2. Zerar lista de sorteio')
        print('\t 3. Ver lista de sorteio')
        print('\t 4. Sortear')
        print('\t 5. Sair')

    def adicionar_nome_ao_sorteio(self):
        os.system('clear')
        nome = input('Digite o nome que deseja adicionar: ')
        self.lista_de_nomes.append(nome)
        input('Aperte qualquer tecla para continuar...')

    def zerar_lista_de_sorteio(self):
        self.lista_de_nomes = []

    def ver_lista_de_sorteio(self):
        os.system('clear')
        for nome in self.lista_de_nomes:
            print('\t' + nome)
        input('Aperte qualquer tecla para continuar...')
        
    def sortear(self):
        os.system('clear')
        print(random.choice(self.lista_de_nomes))
        input('Aperte qualquer tecla para continuar...')

    def sair(self):
        self.terminado = True

app = App()

while not app.terminado:
    app.imprimir_menu()
    opcao = input('Digite a opção escolhida: ')    
    if opcao == '1':
        app.adicionar_nome_ao_sorteio()
    elif opcao == '2':
        app.zerar_lista_de_sorteio()
    elif opcao == '3':
        app.ver_lista_de_sorteio()
    elif opcao == '4':
        app.sortear()
    elif opcao == '5':
        app.sair()
    else:
        print('Opção inválida')