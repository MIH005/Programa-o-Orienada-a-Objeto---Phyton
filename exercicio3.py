#3. Sistema de Biblioteca
#Descrição: Desenvolva uma classe Livro com atributos para título,
#autor, ano de publicação e disponibilidade. Adicione métodos
#para emprestar e devolver o livro, alterando seu status de
#disponibilidade.

class Livro:
    def __init__(self, titulo, autor, ano_publi, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.ano_publi = ano_publi
        self.quantidade = quantidade
        self.status = True

    def emprestar(self, titulo, quantidade):
        if self.status and self.quantidade > 0:
            self.quantidade -= 1
            if self.quantidade == 0:
                self.status = False
            print(f'Livro "{self.titulo}" emprestado com sucesso.')
        else:
            print(f'Livro "{self.titulo}" não está disponível para empréstimo.')

    def devolver(self):
        self.quantidade += 1
        self.disponivel = True
        print(f'Livro "{self.titulo}" devolvido com sucesso.')

    def info(self):
        print(f'Título: {self.titulo}')
        print(f'Autor: {self.autor}')
        print(f'Ano de Publicação: {self.ano_publi}')
        print(f'Quantidade Disponível: {self.quantidade}')
        print(f'Disponível: {"Sim" if self.status else "Não"}')


livro1 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943, 3)
livro1.emprestar("O Pequeno Principe", 2)
livro1.info()