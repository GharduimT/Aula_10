#utilização ou uso de bibliotecas
#biblioteca de acesso randômico
#para numeros aleatorios

# import random
# n = random.randint(1, 10)
# print(n) '''vai gerar numéros de forma aleatória dentro desse intervalo 1, 10 início e fim'''

# import random
# n = random.randint(1, 5)
# m = random.randint(1, 5)
# print(n, m)

# import random
# n = random.randint(1, 5)
# m = random.randint(1, 5)
# print(n, m)

# list_numbers = [random.randint(1, 10)for i in range(5)]
# print(list_numbers)

# import random
# import os
# n = random.randint(1, 5)
# m = random.randint(1, 5)
# print(n, m)

# os.system('cls')
# list_numbers = [random.randint(1, 10)for i in range(5)]
# print(list_numbers)

import random
import os

os.system('cls')
# n = random.randint(1, 5)
# m = random.randint(1, 5)
# print(n, m)

# list_numbers = [random.randint(1, 10)for i in range(5)]
# print(list_numbers)


'''EXEMPLO 02 - FUNÇÃO'''

def gerar_numeros (i, f, q):
    lst_num = [random.randint(i, f) for num in range(q)]
    return lst_num 

ini = int(input('Informe o primeiro número do intervalo: '))
fim = int(input('Informe o último número do intervalo: '))
qdt = int(input('Quantos números? '))

numeros = gerar_numeros(ini, fim, qdt)
print(numeros)
