km = int(input('Qual sua atual velocidade? '))
if km > 80:
	print('Você foi multado!!')
	kmacima = km - 80
	multa = float(kmacima * 7)
	print(f'Multa de R$7,00 por cada km acima de 80, resultando em R${multa} por {kmacima}km a mais do limite')
else:
	print('Você esta nas normas, Boa Viagem :)')