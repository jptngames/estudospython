# Calculadora simples em Python
from math import sqrt
from math import hypot
from math import pow
opcao = 0
while opcao != 8:
    print("""    1 - Soma
    2 - Subtração
    3 - Multiplicação
    4 - Divisão
    5 - Potencia
    6 - Raiz Quadrada
    7 - Hipotenusa
    8 - Sair""")
    opcao = int(input('Qual operação você deseja: '))
    if opcao == 1:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        print('='*12)
        sum = n1 + n2
        print(f'A soma de {n1} + {n2} é {sum}')
        print('='*12)
    elif opcao == 2:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        sub = n1 - n2
        print('='*12)
        print(f'A subtração de {n1} - {n2} é {sub}')
        print('='*12)
    elif opcao == 3:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        mul = n1 * n2
        print('='*12)
        print(f'A multiplicação de {n1} x {n2} é {mul}')
        print('='*12)
    elif opcao == 4:
        n1 = int(input('Digite o primeiro número: '))
        n2 = int(input('Digite o segundo número: '))
        div = n1 / n2
        print('='*12)
        print(f'A divisão de {n1} / {n2} é {div}')
        print('='*12)
    elif opcao == 6:
        n1 = int(input('Digite algum numero para ver a raiz quadrada: '))
        raiz = sqrt(n1)
        print('='*12)
        print(f'A raiz quadrada de {n1} é {raiz:.2f}')
        print('='*12)
    elif opcao == 7:
        co = float(input('Digite o cateto oposto: '
    ))
        ca = float(input('Digite o cateto adjacente: '))
        hi = hypot(co, ca)
        print('='*12)
        print(f"""Calculo feito com sucesso
Cateto Oposto {co:.2f}
Cateto Adjacente {ca:.2f}
Hipotenusa {hi:.2f}""")
        print('='*12)
    elif opcao == 8:
        print('Saindo...')
        break
    elif opcao == 5:
        n1 = int(input('Digite o numero base: '))
        n2 = int(input('Digite o expoente: '))
        po = pow(n1, n2)
        print('='*12)
        print(f'A potenciação com numero base {n1} e expoente {n2} é {po}')
        print('='*12)