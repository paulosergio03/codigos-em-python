salario = float(input('Qual o sálario do funcionário? R$'))
aumento = salario + (salario * 15/100)
print(f'Um funcionário que ganhava {salario:.2f}, com 15% de aumento, passa a receber R${aumento:.2f}')