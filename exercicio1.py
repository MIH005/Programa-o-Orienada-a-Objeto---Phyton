#1. Controle de Estoque
#Descrição: Implemente uma classe Produto com atributos para
#nome, preço e quantidade em estoque. Adicione métodos para
#adicionar e remover produtos do estoque, e um método para
#imprimir as informações do produto.

class Produto:
    def __init__(self,nome,preco,quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def adicionar(self, quantidade):
        self.quantidade += quantidade
    
    def remover(self, quantidade):
            self.quantidade -= quantidade

    def info(self):
        print(f'Nome: {self.nome}')
        print(f'Preço: {self.preco}')
        print(f'Quantidade: {self.quantidade}')

produto1 = Produto("macarrao", 5, 60)
prod2 = Produto("Leite", 8, 40)


