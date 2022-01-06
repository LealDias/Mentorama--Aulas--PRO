#Programa Principal

from multiplos_func import cinco_sete #Importação do Arquivo multiplos_func para verificação dos multiplos

while True:


    print("-------BEM VINDO AO PROGRAMA MULTIPLOS-------")
    print("MULTIPLOS DE 5 = FIZZ")
    print("MULTIPLOS DE 7 = BUZZ")
    print("MULTIPLOS DE AMBOS = FIZZBUZZ")
    print("NÃO MULTIPLOS DE AMBOS = MISS")
    print("--------------------------------------------", end='\n')


    natural = int(input("Insira uma número natural: "))
    cinco_sete(natural)

    res = str(input("Deseja Continuar?: (S/N) "))

    if res == 'S':
        pass

    else:
        break

print("Programa Finalizado....")

#Nesta Etapa não me preocupei muito em tratar os erros e exceções, no entanto concordo que caberia uma série de tratamentos nesta etapa.

    

