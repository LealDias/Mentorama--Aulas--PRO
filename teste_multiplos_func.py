import pytest #-> Importação da biblioteca pytest
from multiplos_func import cinco_sete #-> Importação da biblioteca multiplos_func para execução da função cinco_sete que avalia multiplos de 5 e 7


class Testemultiplos: #Importante: Upper Case na Primeira Letra da Classe é obrogatório

    def setup(self):
        pass

    def test_cinco_sete(self): #-> Função para Execução dos Testes

        resultado = cinco_sete(25)
        resultado1 = cinco_sete(14)
        resultado2 = cinco_sete(35)
        resultado3 = cinco_sete(8)

        assert resultado == 'FIZZ' #-> Resultados Esperados
        assert resultado1 == 'BUZZ'
        assert resultado2 == 'FIZZBUZZ'
        assert resultado3 == 'MISS'



