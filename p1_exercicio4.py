## maior sequencia consecutiva de números em ordem crescente tem count_A elementos.
## maior sequencia consecutiva de números constantes tem count_B elementos.

count_A = 1
count_maximo_A = 1
count_B = 1
count_maximo_B = 1
soma = 0
soma_maxima = 0
elemento_constante = -10
elemento_constante_maximo = -10
n_antecessor = -10
# lista = [7,7,7,6,6,6]

# for i in lista:
for i in range(150):
    n_sucessor = int(input('Digite um número: '))
    # n_sucessor = i
    if n_antecessor == -10 or n_sucessor != n_antecessor + 1:
        soma = n_sucessor
        count_A = 1
    if n_sucessor == n_antecessor + 1:
        soma = soma + n_sucessor
        count_A = count_A + 1
    if count_A > count_maximo_A:
        count_maximo_A = count_A
        soma_maxima = soma
    if count_A == count_maximo_A:
        if soma > soma_maxima:
            soma_maxima = soma
    if n_antecessor == -10 or n_sucessor != n_antecessor:
        count_B = 1
    if n_antecessor == n_sucessor:
        count_B = count_B + 1
        elemento_constante = n_antecessor
    if count_B > count_maximo_B:
        count_maximo_B = count_B
        elemento_constante_maximo = n_antecessor
    if count_B == count_maximo_B:
        if elemento_constante > elemento_constante_maximo:
            elemento_constante_maximo = elemento_constante 
    n_antecessor = n_sucessor

print(f'a maior sequencia consecutiva de números em ordem crescente tem {count_maximo_A} elementos, a soma máxima é {soma_maxima}')
print(f'a maior sequencia consecutiva de número constantes tem {count_maximo_B} elementos. Dentre a(s) maior(es) sequencia(s), o maior elemento constante é {elemento_constante_maximo}')