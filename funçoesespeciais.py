# funçoes lambda(anonimas)
# sintaxe
# lambda argumentos: expressao

# quadrado = lambda x: x ** 2
#
# for i in range(11):
#     print(quadrado(i))

# par = lambda x: x % 2 ==0
#
# print(par(4))

# f_c = lambda f: (f - 32) * 5 / 9
# print(f_c(80))

# Função map

# sintaxe
# map(função, iteravel)

# num = list(range(11))
# dobro = list(map(lambda x: x*2, num))
# print(dobro)
#

# palavras = ['Python', 'é', 'uma', 'linguagem', 'de', 'programação']
# upper = list(map(str.upper, palavras))
# print(upper)

# Função filter()
# Sintaxe:
# Filter(função, sequencia)

# def numeros_pares(n):
#     return n % 2 == 0
#
# numeros = [1,2,3,4,5,6,7,8,9,10]
#
# num_par = list(filter(numeros_pares, numeros))
# print(num_par)

# numeros = [1,2,3,4,5,6,7,8,9,10]
# num_impar = list(filter(lambda x: x % 2 != 0, numeros))
#
# print(num_impar)

# Função reduce()
# sintaxe
# reduce(função, sequencia, valor_inicial)

from functools import reduce

# def mult (x, y):
#     return x * y
#
# numeros = [1,2,3,4,5,6]
#
# total = reduce(mult, numeros)
# print(total)

# Soma cumulativa dos quadrados de valores, usando expressão lambda

numeros = [1,2,3,4]

total = reduce(lambda x, y: x ** 2 + y **2, numeros)
print(total)