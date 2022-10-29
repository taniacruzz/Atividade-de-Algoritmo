#exercício 5 da p1 
soma_par_h = 0
soma_impar_h = 0
soma_par_s = 0
soma_impar_s = 0

soma_p = 0
numero_primo = 1
numero_impar = 1

n = int(input('N = ')) # o usuário vai dar um número para n

if n >= 50: # verificando se n tem valor >= 50
    for i in range(n):# para um intervalo de 0 a n: 
        #Calculando P:
        auxiliar = 0
        while auxiliar == 0:
            quantidade_divisores = 0
            numero_primo += 1
            for divisor in range(1, numero_primo + 1):
                if numero_primo % divisor == 0:
                    quantidade_divisores += 1
            if quantidade_divisores == 2:
                auxiliar = 1
        soma_p += (numero_primo/(numero_impar**3))
        numero_impar += 2
        #Calculando H e S:
        while n > 1:
            soma_h = 1 #começa a soma com 1, pois vamos indicar se n é par ou impar e para 1/1 sempre será positivo
            soma_s = 1 # o mesmo caso de cima
            if n % 2 == 0:
                soma_par_h += (n*2-1)/n
                soma_par_s += -(n/(n*n))
            if n % 2 != 0:
                soma_impar_h += -((n*2-1)/n)
                soma_impar_s += n/(n*n)
            soma_h += soma_par_h + soma_impar_h
            soma_s += soma_par_s + soma_impar_s
            n -= 1
    #SAÍDAS:
    #print('\nH:\nsoma par {}\nsoma impar {}\nsoma {}\n'.format(soma_par_h, soma_impar_h, soma_h))
    #print('S:\nsoma par {}\nsoma impar {}\nsoma {}\n'.format(soma_par_s, soma_impar_s, soma_s))
    #print('P:\nsoma {}\n'.format(soma_p))
    print('H = {}\nS = {}\nP = {}\n'.format(soma_h, soma_s, soma_p))
else:
    print('N tem que ser maior ou igual a 50')