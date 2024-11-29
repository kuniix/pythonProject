# Recursividade

# Formula geral para o fatorial:
# fatorial(num) = 1, se num = 0 ou se num = 1 'Caso-base'
# fatorial(num) = num * fatorial(num -1), para num > 1 'Caso recursivo'
# 4! > 4 * fatorial(3)


def fatorial(numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)

if __name__ == '__main__':
    x = int(input('Digite um número inteiro: '))
    try:
        resultado = fatorial(x)
    except RecursionError:
        print('O número fornecido é muito grande ou negativo')
    else:
        print(f"O fatorial de {x} é {resultado}")


