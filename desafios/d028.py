from random import randrange
nc = randrange(6)
nh = int(input('Adivinhe o número que a maquina escolheu: '))
if nc == nh:
	print(f"""Parabéns, vc acertou!!
Número da maquina: {nc}
Seu número: {nh}""")
else:
		print(f"""Poxa, vc errou ;-;
Número da maquina: {nc}
Seu número: {nh}""")
