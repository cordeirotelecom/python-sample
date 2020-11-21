# Projeto de uma calculadora em Phyton

def calculadora():
    operador = input('''
Exemplo: 1 + 1
Resultado: 2

OPERADORES:
+ para adição
- subtração
* multiplicação'
/ divisão
''')
    
    numero_1 = float(input('Entre com o primeiro número: '))
    numero_2 = float(input('Entre com o segundo número: '))

    if operacao == '+':
        print('{} + {} = '.format(numero_1, numero_2))
        print(numero_1 + numero_2)

    elif operacao == '-':
        print('{} - {} = '.format(numero_1, numero_2))
        print(numero_1 - number_2)

    elif operacao == '*':
        print('{} * {} = '.format(numero_1, numero_2))
        print(numero_1 * number_2)

    elif operacao == '/':
        print('{} / {} = '.format(numero_1, numero_2))
        print(numero_1 / number_2)

    else:
        print('Você não entrou com uma operação válida, por favor rode o programa novamente.')

    novamente()

def novamente():
    calc_novamente = input('''
Você deseja calcular novamente?
"S" para sim, "N" para não.
''')

    if calc_novamente.upper() == 'S':
        calculadora()
    elif calc_novamente.upper() == 'N':
        print('Vá com Deus! Deus te Ilumine!')
    else:
        novamente()

calculadora()
