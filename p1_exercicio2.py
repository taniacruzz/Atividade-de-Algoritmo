salario_fixo = float(input('Qual o salario fixo: '))
vendas = float(input('Qual o valor das vendas: '))
if vendas <= 1500:
    salario_final = salario_fixo + 0.05*vendas
if vendas > 1500:
    diferenca = vendas - 1500
    salario_final = salario_fixo + 0.05*1500 + 0.07*diferenca
print(f'O salario final é {salario_final} reais')