dias = float(input('Quantos dias? '))
km = float(input('Quantos Km foram percorridos? '))
pago = (dias * 60) + (km * 0.15)
print(f'O total a pagar é de R${pago:.2f}')
