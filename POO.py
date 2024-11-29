# Orientação a objetos: paradigma de programação
# Classes e objetos

class Veiculo:
    def movimentar(self):
        print(f"Sou um veiculo em movimento!")

    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None

    # Getter
    def get_fbr_modelo(self):
        return f'Fabricante: {self.__fabricante}, Modelo: {self.__modelo}'

    def get_num_registro(self):
        return self.__num_registro

    # Setter
    def set_num_registro(self, registro):
        self.__num_registro = registro


class Carro(Veiculo):
    # Método init sera herdado
    def movimentar(self):
        print(f"Sou um carro em movimento!")


class Motoca(Veiculo):
    def movimentar(self):
        print(f"To dando grau de motoca")


class Aviao(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__categoria = categoria
        super().__init__(fabricante, modelo)

    def get_categoria(self):
        return self.__categoria

    def movimentar(self):
        return 'O pai ta voando'


class Caminhao(Veiculo):
    def __init__(self, fabricante, modelo, capacidade):
        self.__capacidade = capacidade
        super().__init__(fabricante, modelo)

    def movimentar(self):
        return 'Sai da frnte que o caminhão ta passando'

    def get_capacidade(self):
        return self.__capacidade


if __name__ == '__main__':
    meu_veiculo = Veiculo('Ford', 'Fusion')
    meu_veiculo.movimentar()
    print(meu_veiculo.get_fbr_modelo())
    meu_veiculo.set_num_registro(1998)
    print(meu_veiculo.get_num_registro())
    print('=' * 20)

    meu_carro = Carro('Toyota', 'Corolla')
    meu_carro.movimentar()
    print(meu_carro.get_fbr_modelo())
    meu_carro.set_num_registro(2010)
    print(meu_carro.get_num_registro())
    print(meu_carro.get_fbr_modelo(), meu_veiculo.get_num_registro())
    print('=' * 20)

    minha_moto = Motoca('Kawasaki', 'Ninja')
    minha_moto.movimentar()
    minha_moto.set_num_registro(2012)
    print(minha_moto.get_fbr_modelo(), minha_moto.get_num_registro())
    print('=' * 20)

    meu_aviao = Aviao('Boeing', '747', 'Comercial')
    print(meu_aviao.movimentar())
    print(meu_aviao.get_fbr_modelo())
    print('Tipo: ', meu_aviao.get_categoria())
    print('=' * 20)

    meu_caminhao = Caminhao('Volvo', 'A230', '50 Toneladas')
    print(meu_caminhao.movimentar())
    print('Capacidade: ', meu_caminhao.get_capacidade())








