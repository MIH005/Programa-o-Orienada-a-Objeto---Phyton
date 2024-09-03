#2. Gerenciamento de Pessoas
#Descrição: Crie uma classe Pessoa com atributos para nome,
#idade e endereço. Inclua métodos para alterar o endereço e
#outro para exibir todas as informações da pessoa.

class Pessoas:
    def __init__(self, nome, idade, endereco):
        self.nome = nome
        self.idade = idade
        self.endereco = endereco

    def alterar(self, endereco):
        self.endereco = endereco
    
    def info(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Endereço: {self.endereco}')

pessoa1 = Pessoas("Emilly", 19, "R.Olimpia de Almeida Prado")

pessoa1.alterar("barao de limeira")
print(pessoa1.endereco)
    