#exercício 5 da p1 
soma_h = 0 
soma_s = 0 
soma_p = 0
numero_primo = 1
numero_impar = 1

n = int(input('N = ')) # o usuário vai dar um número para n

if n >= 50: # verificando se n tem valor >= 50
    for i in range(n):# para um intervalo de 0 a (n-1): 
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
        if i == 0:
            soma_h = 1
            soma_s = 1
        if i % 2 == 0 and i !=0:
            soma_h += -((i+1)*2-1)/(i+1)
            soma_s += ((i+1)/((i+1)*(i+1)))
        if i % 2 != 0:
            soma_h += (((i+1)*2-1)/(i+1))
            soma_s += -((i+1)/((i+1)*(i+1)))
    print('H = {}\nS = {}\nP = {}\n'.format(soma_h, soma_s, soma_p))
else:
    print('N tem que ser maior ou igual a 50')