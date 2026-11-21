
class Livro:
    def __init__(self,nome='???',paginas=0,unidades=0,genero='???'):
        self.nome=nome
        self.paginas=paginas
        self.unidades=unidades
        self.genero=genero
# cateristica do livo


class Estante:
    def __init__(self):
        self.nome={}
        self.quantidade={}
    def add_livro (self,livro):
        if livro.genero not in self.quantidade:
            self.quantidade[livro.genero]=0
        for lv,n in self.quantidade.items():
            if lv==livro.genero:
                self.quantidade[lv]+=livro.unidades

    def __str__(self):
        return f'{self.quantidade}'

live1=Livro('a vida',10,5,'terror')
istante=Estante()
istante.add_livro(live1)

print(istante)

