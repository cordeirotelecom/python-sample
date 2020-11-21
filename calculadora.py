''' Projeto de uma calculadora em Phyton '''

# -*- coding: utf-8 -*-

import math

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
    
    try:
    numero_1 = float(input('Entre com o primeiro número: '))
    numero_2 = float(input('Entre com o segundo número: '))
    
    except ValueError:
    print("Digite somente números, sem letras")
    calculadora()

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
    
    elif operacao == 'raiz {}':
        raiz = math.sqrt(num)
        print(f'\nA raiz quadrada de {num} é {raiz}\n')
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
