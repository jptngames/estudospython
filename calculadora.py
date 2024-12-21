printmath import sqrt, hypot, pow

def soma(x, y):
    result = x + y
    print(f'A soma de {x} + {y} é {result}')

def sub(x, y):
    result = x - y
    sep(12)
    print(f'A subtração de {x} - {y} é {result}')

def multi(x, y):
    result = x * y
    sep(12)
    print(f'A multiplicação de {x} × {y} é {result}')

def div(x, y):
    result = x / y
    sep(12)
    print(f'A divisão de {x} ÷ {y} é {result}')

def po(x, y):
    result = pow(x, y)
    sep(12)
    print(f'A potenciação com base {x} e expoente {y} é {result}')

def sqr(x):
    result = sqrt(x)
    sep(12)
    print(f'A raiz quadrada de {x} é {result}')

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
    match opcao:
        case 1:
            sep(12)
            soma(float(input('Qual o primeiro número? ')), float(input('Qual o segundo número? ')))
            sep(15)
    
        case 2:
            sep(12)
            sub(float(input('Qual o primeiro número? ')), float(input('Qual o segundo número? ')))
            sep(15)
        
        case 3:
            sep(12)
            multi(float(input('Qual o primeiro número? ')), float(input('Qual o segundo número? ')))
            sep(15)
        
        case 4:
            sep(12)
            div(float(input('Qual o primeiro número? ')), float(input('Qual o segundo número? ')))
            sep(15)
        
        case 5:
            sep(12)
            po(float(input('Qual o número base? ')), float(input('Qual o expoente? ')))
            sep(15)
        
        case 6:
            sep(12)
            sqr(float(input('Qual número você deseja ver a Raiz Quadrada? ')))
            sep(15)
        
        case 7:
            sep(12)
            co = float(input('Digite o cateto oposto: '))
            ca = float(input('Digite o cateto adjacente: '))
            hi = hypot(co, ca)
            sep(12)
            print(f"""Calculo feito com sucesso
Cateto Oposto {co:.2f}
Cateto Adjacente {ca:.2f}
Hipotenusa {hi:.2f}""")
            sep(15)
        
        case 8:
            print('Saindo...')
            break
        
        case _:
            sep(12)
            print('Opção Inválida')
            sep(15)