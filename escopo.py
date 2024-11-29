#Escopo global e local

var_global = 'Curso completo de Python'


def escreve_texto():
    var_local = 'Lucas Norato'
    global var_global
    var_global = 'Banco de dados com sql'
    print(f'Variavel global: {var_global}')
    print(f'Variavel local {var_local}')


if __name__ == '__main__':
    print(f'Executar a função escreve_texto(0')
    escreve_texto()

    print('Tentar acessar as variaveis diretamente')
    print(f"Variavel Global: {var_global}")
    # print(f"Variavel local: {var_local}")

