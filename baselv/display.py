import tkinter as tk

class Janela:
    """A classe Janela é a base onde o programa é exibido. Dentro dela,
          existem outras duas classes, E_aria e D_aria,
          que são responsáveis por exibir o conteúdo do programa.
          A classe E_aria representa a área esquerda,
         enquanto a D_aria representa a área direita. Além disso,
         a classe Janela também define o tamanho da janela e o seu título."""
    def __init__(self):
        self.painel=tk.Tk()
        self.painel.title('Organizador de livros.')
        self.painel.geometry('600x400')
        self.painel.resizable(False,False)

        self.pain1=E_area(self.painel)
        self.pain2=D_area(self.painel)

    def mostra_janela(self):
        """Mantenha a janela aberta e coloque essa função sempre no final do programa."""
        self.painel.mainloop()

class E_area:
    """A classe E_area serve para armazenar as informações
      que serão adicionadas pelo usuário. Foram adicionados os recursos 
      necessários para que esses dados possam ser armazenados."""
    def __init__(self,janela):
        self.frame=tk.Frame(janela,bg="#C5D3D3",width=200,height=200)
        self.frame.pack(side="left",padx=10,pady=10,expand=True,fill='both')

        self.tx1=tk.Label(self.frame,text='nome do livro:',font=('Arial',12),)
        self.tx1.grid(row=0,column=0)
        self.nome_livro=tk.Entry(self.frame)
        self.nome_livro.grid(row=0,column=1)

class D_area:
    def __init__(self,janela):
        self.frame=tk.Frame(janela,bg="#C5D3D3",width=200,height=200)
        self.frame.pack(side="right",padx=10,pady=10,expand=True,fill='both')