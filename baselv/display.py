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

        self.validacao=self.frame.register(self.validar)#Validar entrada somente de números. 
        self.validacao_letra=self.frame.register(self.validar_letra) #Validar entrada somente de letras.


        #A entrada onde o usuário vai digitar o nome do livro.
        self.tx1=tk.Label(self.frame,text='nome do livro:',font=('Arial',12),bg="#C5D3D3")
        self.tx1.grid(row=1,column=0)
        self.nome_livro=tk.Entry(self.frame)
        self.nome_livro.grid(row=1,column=1)
        self.nome_livro.bind("<KeyRelease>",lambda event:self.verificar_botao())

        #A entrada onde o usuário digita a quantidade de unidades.
        self.tx2=tk.Label(self.frame,text='unidades do livro:',font=('Arial,12'),bg="#C5D3D3")
        self.tx2.grid(row=2,column=0,pady=10)
        self.quantidade_livros=tk.Entry(self.frame,validate="key",validatecommand=(self.validacao,"%P"))
        self.quantidade_livros.grid(row=2,column=1)
        self.quantidade_livros.bind("<KeyRelease>",lambda event:self.verificar_botao())

        #A entrada onde o usuário digita o gênero do livro.
        self.tx3=tk.Label(self.frame,text='genero do livro:',font=('Arial',12),bg="#C5D3D3")
        self.tx3.grid(row=3,column=0)
        self.genero_livro=tk.Entry(self.frame,validate="key",validatecommand=(self.validacao_letra,"%P"))
        self.genero_livro.grid(row=3,column=1)
        self.genero_livro.bind("<KeyRelease>",lambda event:self.verificar_botao())

        #A entrada onde o usuário digita a quantidade de páginas.
        self.tx4=tk.Label(self.frame,text='quantidade de paginas:',font=('Arial',12),bg="#C5D3D3")
        self.tx4.grid(row=4,column=0,pady=10)
        self.paginas_livro=tk.Entry(self.frame,validate="key",validatecommand=(self.validacao,"%P"))
        self.paginas_livro.grid(row=4,column=1)
        self.paginas_livro.bind("<KeyRelease>",lambda event:self.verificar_botao())

        # incompleto
        self.botao_salvar=tk.Button(self.frame,text='salvar',state="disabled")
        self.botao_salvar.grid(row=5,column=1)



    def validar (self,valor):
            '''ele e  usado na self.validacao'''
            return (valor.isdigit() and len(valor)<=6) or valor==""
    
    def validar_letra(self,valor):
         '''ele e usado na self.validacao_latra'''
         return valor.isalpha() or valor==""

    
    def verificar_botao(self):
        """Esse `def` verifica se todas as entradas estão preenchidas
           para liberar o botão de salvar."""
        if self.nome_livro.get() and self.quantidade_livros.get() and self.genero_livro.get() and self.paginas_livro.get():
             self.botao_salvar.config(state="normal")
        else:
             self.botao_salvar.config(state="disabled")



class D_area:
    def __init__(self,janela):
        self.frame=tk.Frame(janela,bg="#C5D3D3",width=200,height=200)
        self.frame.pack(side="right",padx=10,pady=10,expand=True,fill='both')