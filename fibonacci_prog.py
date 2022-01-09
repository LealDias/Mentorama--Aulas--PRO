#----------------------------------------------------------------------------------------------------------------# -> Classe

class Fibonacci_Iterador: # -> Criação da Classe Fibonacci_Iterador, que possui a função de gerar a sequência de fibonacci através de uma sequência de n iterações.
    

    def __init__(self, iteracao): # -> Método Construtor da Classe

        self.iteracao = iteracao
        self.anterior = 0
        self.proximo  = 1

    def __iter__(self): # -> Iterador
        
        self.iteracao = self.iteracao
        
    def __next__(self):
        
        try: # -> Tratamento de Exceção para casos onde o usuário digita um valor menor que 1
            
            if self.iteracao < 1:
                raise StopIteration
                
            elif self.iteracao == 1:    
                
                valores = list()
                valores.append(self.anterior)

            else:        
        
                valores = list((0, 1))
        
                for i in range(self.iteracao - 2): # -> loop for para segregação/agrupamento dos valores gerados pelo objeto self.proximo
                
                    res = self.proximo + self.anterior
                    self.anterior = self.proximo 
                    self.proximo = res
                    self.iteracao -= 1
                
                    valores.append(self.proximo)
                    
            return valores # -> Retorna os valores dentro da lista
            
        except StopIteration:
            
                print("Valor Inválido para a Classe!!!!")



#----------------------------------------------------------------------------------------------------------------# -> Rodando o Programa Principal


try: #Foi aplicado um tratamento de exceção
    
    fibo = Fibonacci_Iterador(20) # Instância da Classe 'Fibonacci_Iterador (anterior, proximo, iterecao)'
    numeros = {k: v for k, v in enumerate((next(fibo)))}
    print(f'Os {len(numeros)} primeiros números da Sequência de Fibonacci São {numeros}')
    
except TypeError:
    
    print("Você Inseriu um Valor Igual ou Menor do que Zero...ou Inseriu Argumentos Errados!")
 
 #----------------------------------------------------------------------------------------------------------------# -> Fim do Programa Principal...  