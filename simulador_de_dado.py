#Siulador de dado
#Simular o uso de um dado, gerando um valor de 1 até 6
import random
import PySimpleGUI

class SimuladorDeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Voce gostaria de gerar um novo valor para o dado?'

    def Iniciar(self):
        resposta = input(self.mensagem)
        try:    
            if resposta == 'sim' or resposta == 's':
                 self.GerarValorDoDado()
            elif resposta == 'não' or resposta == 'n':
                print('Agradecemos a sua participação!')
            else:
                print('Favor digite sim ou nao!')
        except: 
                print('Ocorreu um erro na sua resposta')
    def GerarValorDoDado(self):
                print(random.randint(self.valor_minimo, self.valor_maximo))

simulador = SimuladorDeDado()
simulador.Iniciar()

