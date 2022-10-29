#exercício 3 da p1
pop_a1 = 15000 #total população da cidade A no ano zero, usar no primeiro caso
pop_a2 = 15000 #total população da cidade A no ano zero, usar no segundo caso
pop_b = 45000 #total população da cidade B no ano zero
pop_c = 65000 #total população da cidade C no ano zero

anos1 = 0 #contador de anos para quando a pop. de A >= B
anos2 = 0 #contador de anos para quando a pop. de A > C em 23%

while pop_a1 < pop_b: #enquanto a população de A for menor que a de B, execute:
    pop_a1 += pop_a1 * 0.1 #incremento anual de 10% da população A
    pop_b += pop_b * 0.05 #incremento anual de 5% da população B
    anos1 += 1 #contando os anos que leva para A >= B
print('\nA população de A se iguala ou ultrapassa a população de B em {} anos.\n'.format(anos1)) # mostra o resultado do contador

while ((pop_a2-pop_c)/pop_c ) <= 0.23: #enquanto a porcentagem da população de A sobre a C for <= a 23%, execute:
    pop_a2 += pop_a2 * 0.1 #incremento anual de 10% da população A
    pop_c += pop_c * 0.025 #incremento anual de 2,5% da população C
    anos2 += 1 #contando os anos que leva para A > C em 23% de C
print('A população de A ultrapassa a população de C em 23 por cento em {} anos.\n'.format(anos2)) # mostra o resultado do contador