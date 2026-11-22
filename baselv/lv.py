
class Livro:
    """A classe `Livro` serve como um item a ser manipulado pelas outras classes.
      Nela, você pode adicionar todas as características de um livro, como nome, gênero,
      quantidade de páginas e número de cópias disponíveis."""
    def __init__(self,nome='???',paginas=0,unidades=0,genero='???'):
        self.nome=nome
        self.paginas=paginas
        self.unidades=unidades
        self.genero=genero
# cateristicas dos  livos


class Estante:
    def __init__(self):
        self.nome={}
        self.quantidade={}

    def add_livro (self,livro):
        """O add_livro serve para adicionar um objeto da classe Livro à classe Estante.
          A classe Estante vai armazenar os livros em dois dicionários, organizados por gênero.

          O primeiro dicionário vai separar a quantidade de livros por gênero,
          enquanto o segundo vai armazenar o nome dos livros, também separados por gênero."""
        if livro.genero not in self.quantidade:
            self.quantidade[livro.genero]=0
        self.quantidade[livro.genero]+=livro.unidades
        if livro.genero not in self.nome:
            self.nome[livro.genero]=[]
        self.nome[livro.genero].append(livro.nome)

    def __str__(self):
        return f'{self.quantidade} {self.nome}'

live1=Livro('a vida',10,5,'terror')
live2=Livro('o olho',11,1,'terror')
livo3=Livro('amor',100,40,'romence')
istante=Estante()
istante.add_livro(live1)
istante.add_livro(live2)
istante.add_livro(livo3)
print(istante)

