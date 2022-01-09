import pytest
from fibonacci_prog import Fibonacci_Iterador

class Teste_Fibonacci:

    def setup(self):
        pass
 #------------------------------------------------------------------------------------------------------------------------------------> TESTE 1 - Iteraçao == 2

    def test_next_1(self): # -> Teste do Iterador com o retorno Esperado pela função __next__()

        f = Fibonacci_Iterador(2) # -> Parametros da Função Fibonacci_Iterador(anterior, proximo, iteracao)
        resultado = next(f)
        assert resultado == [0, 1] # -> Resultado retorna uma lista com os dois primeiros números da sequência

 #------------------------------------------------------------------------------------------------------------------------------------> TESTE 2 - Iteração == 1

    def test_next_2(self):

        g = Fibonacci_Iterador(1) # -> Parametros da Função Fibonacci_Iterador(anterior, proximo, iteracao)
        resultado = next(g)
        assert resultado == [0] # -> Resultado retorna uma lista com apenas o primeiro número da sequência

#------------------------------------------------------------------------------------------------------------------------------------> TESTE 3 - Erro de Iteração (Quando o Iterador é igual a zero)
    def test_erro_stop(self):

        h = Fibonacci_Iterador(0)
        resultado = next(h)
        assert resultado == print("Valor Inválido para a Classe!!!!")

#------------------------------------------------------------------------------------------------------------------------------------> TESTE 4 - Erro de Tipo, quando são iseridos mais do que 1 Parâmetro

    def test_type_erro(self):

        try:
            Fibonacci_Iterador(1, 6)

        except TypeError:
            AssertionError 

 #------------------------------------------------------------------------------------------------------------------------------------> FIM DOS TESTES       
    

    
