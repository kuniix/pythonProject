#Exceção é um objeto que represeta um erro que ocorreu no programa
#blocos Try ... except


def div(k, j):
    return round(k / j, 2)

if __name__ == '__main__':
    while True:
        try:
            n1 = int(input('Digite um número: '))
            n2 = int(input('Digite outro número: '))
            break
        except ValueError:
            print('Ocorreu um erro ao ler o valor, tente novamente!')

    try:
        r = round(n1 / n2)
    except ZeroDivisionError:
        print('Ocorreu um erro ao dividir por zero!')
    except:
        print('Ocorreu um erro desconhecido')
    else:
        print(f'Resultado: {r}')
    finally:
        print('Fim do programa') 



