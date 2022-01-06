def cinco_sete(num):
    

    if (num%5 == 0) and (num%7 == 0):

        res = 'FIZZBUZZ'
        print("FIZZBUZZ")
        return res

    elif num%5 == 0:

        res = 'FIZZ'
        print(res)
        return res

    elif num%7 == 0:

        res = 'BUZZ'
        print('BUZZ')
        return res

    else:

        res = 'MISS'
        print('MISS') 
        return res       

