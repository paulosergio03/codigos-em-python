preco = float(input('Qual o preço do produto? R$'))
desconto = preco - (preco * 5 / 100)

print(f'O preco do produto é R${preco:.2f}, na promoção com desconto de 5% vai custar R${desconto:.2f}')