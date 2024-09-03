#4. Veículo
#Descrição: Implemente uma classe Carro com atributos para
#marca, modelo, ano e quilometragem. Inclua métodos para
#dirigir o carro, que aumenta a quilometragem, e outro método
#para exibir informações do carro.

class Carro:
    def __init__(self, marca, modelo, quilometragem):
        self.marca = marca
        self.modelo = modelo 
        self.quilometragem = quilometragem

    def dirigir(self, kmRodado):
        if kmRodado > 0:
            self.quilometragem += kmRodado
        else:
            print("KM Invalida")
    
    def info(self):
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print(f'Quilometragem: {self.quilometragem}')

carro1 = Carro("Toyota", "Corolla", 15000)
carro2 = Carro("Toyota", "fusca", 200)
carro1.dirigir(100)
carro2.dirigir(5)

carro1.info()
carro2.info()



    
        