
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

    def pegar_livro (self,livro):
        """A função `pegar_livros` serve para retirar uma unidade da classe `Livro`
          e também diminuir em uma unidade a quantidade registrada no dicionário `quantidade`, 
          que fica na classe `Estante`. Além disso, quando a quantidade de um determinado livro
          chega a zero, o nome desse livro é removido do dicionário `nome`."""
        if self.quantidade[livro.genero]>0:
            livro.unidades-=1
            self.quantidade[livro.genero]-=1
        if livro.unidades<=0:
            self.nome[livro.genero].remove(livro.nome)

# Daqui para baixo, são apenas testes; não há problema se forem apagados.
    def __str__(self):
        return f'{self.quantidade} {self.nome}'

live1=Livro('a vida',10,5,'terror')
live2=Livro('o olho',11,1,'terror')
livo3=Livro('amor',100,40,'romence')
istante=Estante()
istante.add_livro(live1)
istante.add_livro(live2)
istante.add_livro(livo3)
istante.pegar_livro(live2)
print(istante)

