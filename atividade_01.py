# criar (com função) calculadora para dois números digitados pelo usuário.
# a calculadora vai somar, subtrai, divide e multiplica

# def soma(a, b):
#     return a + b


# def subtrai(a, b):
#     return a - b


# def divide(a, b):
#     # if b == 0:
#     #     return

#     return a / b


# def multiplica(a, b):
#     return a * b


# num1 = int(input('digite o primeiro numero: '))
# num2 = int(input('digite o segundo numero: '))

# adicao = soma(num1, num2)
# sub = subtrai(num1, num2)
# div = divide(num1, num2)
# mult = multiplica(num1, num2)

# print (adicao, sub, div, mult)

#receber numeros aleatórios
import random


def soma(a, b):
    return a + b


def subtrai(a, b):
    return a - b


def divide(a, b):
    # if b == 0:
    #     return

    return a / b


def multiplica(a, b):
    return a * b

# num1 = int(input('digite o primeiro numero: '))
# num2 = int(input('digite o segundo numero: '
num1 = random.randint(1, 10)
num2 = random.randint(1, 10)

adicao = soma(num1, num2)
sub = subtrai(num1, num2)
div = divide(num1, num2)
mult = multiplica(num1, num2)

print('Estes são os números escolhidos aleatóriamente', num1, 'e', num2)
print('SOMA', adicao, '\n', 'SUBTRAÇÃO', sub, '\n', 'DIVISÃO', div, '\n', 'MULTIPLICAÇÃO', mult)

