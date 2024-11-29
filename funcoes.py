# funçoes = modularização, reuso de codigo, legibilidade
# def <nome_função> ([argumentos]):
#     <instrução>

# def mensagem():
#     print('Bóson treinamentos em Tecnologia')
#     print('Curso completo de Python')
#
# mensagem()

# Função com argumentos

# def soma(a, b):
#     return a+b
#
# print(soma(15, 22))
#
# def multiplicacao(x, y):
#     return x*y
#
# a = 5
# b = 8
# c = multiplicacao(a, b)
#
# print(f"O produto de {a} e {b} é {c}")
#
# def divisao(a, b):
#     if b != 0:
#         return a/b
#     else:
#         return "Impossivel dividir por zero"
#
# if __name__ == '__main__':
#     a = int(input("Digite um número: "))
#     b = int(input("Digite outro número"))
#
#     result = divisao(a,b)
#     print(f'{a} dividido por {b} é igual a {result}')

# def quadrado(val):
#     quadrados = []
#     for x in val:
#         quadrados.append(x**2)
#     return quadrados


def contar(num=11, caractere='+'):
    for i in range(1, num):
        print(caractere)


x = 5
y = 6
z = 3


def soma_mult(a, b, c=0):
    if c == 0:
        return a * b
    else:
        return a + b + c


if __name__ == '__main__':
    contar(num=11, caractere='@')
    contar(6, 'g ')
    # valores = [1,5,4,7,2,3,6]
    # resultados = quadrado(valores)
    # for g in resultados:
    #     print(g)

    print(soma_mult(x, y))
