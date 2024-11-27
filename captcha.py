from random import choice
import string
from rich import print
captchalist = list(string.ascii_uppercase + string.ascii_lowercase + string.digits)
c1 = choice(captchalist)
c2 = choice(captchalist)
c3 = choice(captchalist)
c4 = choice(captchalist)
c5 = choice(captchalist)
c6 = choice(captchalist)
captcha = c1 + c2 + c3 + c4 + c5 + c6

name= input('Qual seu nome? ')
print(f'Eae [blue]{name}[/blue] para continuar coloque o codigo [red]{captcha}[/red] abaixo para verficicação')
verify = input('Qual é o codigo? ')
while captcha != verify:
	c1 = choice(captchalist)
	c2 = choice(captchalist)
	c3 = choice(captchalist)
	c4 = choice(captchalist)
	c5 = choice(captchalist)
	c6 = choice(captchalist)
	captcha = c1 + c2 + c3 + c4 + c5 + c6
	print('Tente novamente!!')
	print(f'Coloque o codigo [red]{captcha}[/red] abaixo para verficicação')
	verify = input('Qual é o codigo? ')
else:
	print(f'Seja bem vindo [blue]{name}[/blue]')
