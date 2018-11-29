from tkinter import *
from tkinter import messagebox
from segunda_janela import Segunda_janela
from terceira_janela import Terceira_janela
from quarta_janela import Quarta_janela
from quinta_janela import Quinta_janela

class Janela_princial(Tk):
    def __init__(self, control):
        super().__init__()
        self.geometry('1000x500+200+200')
        self.title('Concessionária')
        self.control = control
        self.btn_close = Button(self, width=30, text='Sair', command=self.destroy)
        self.btn_close.place(x=750, y=460)
        self.btn_carros = Button(self, width=30, text='Carros', command= self.criar_segunda_janela)
        self.btn_carros.place(x=100, y=460)
        self.btn_compradores = Button(self, width=30, text='Compradores', command= self.criar_terceira_janela)
        self.btn_compradores.place(x=540, y=460)
        self.btn_vendedores = Button(self, width=30, text='Vendedores', command=self.criar_quarta_janela)
        self.btn_vendedores.place(x=320, y=460)
        self.carregar_carros()

    def carregar_carros(self):
        r = 2
        c = 0
        for b in self.control.bd.get_carros():
            Button(self, width=10, text=f'{b.get_placa()}', command=lambda carro=b: self.criar_quinta_janela(carro)).grid(row=r, column=c, pady=5)
            c += 1
            if c == 4:
                c = 0
                r += 1
    def atualizar_patio(self):
        for c in self.grid_slaves():
            if type(c) is Button:
                if c['text'] != 'Sair':
                    c.destroy()
        self.carregar_carros()

    #     self.menu = Menu(self)
    #     self.menu_principal = Menu(self.menu, tearoff=0)
    #     self.menu_principal.add_command(label='Comando 1', command=self.menu_click)
    #     self.menu_principal.add_command(label='Comando 2', command=self.menu_click)
    #     self.menu_principal.add_command(label='Segunda janela', command=self.criar_segunda_janela)
    #     self.menu_principal.add_separator()
    #     self.menu_principal.add_command(label='Sair', command=self.destroy)
    #     self.menu.add_cascade(label='Principal', menu=self.menu_principal)
    #     self.config(menu=self.menu)
    def destroy(self):
        if messagebox.askokcancel('confirmação', 'Deseja sair?'):
            super().destroy()
    def btn_ok_click(self):
        self.lbl_ok['text'] = self.txt_ok.get()

    def menu_click(self):
        nota = open('Nota_fiscal.txt', 'r')



        messagebox.showinfo('Notal fiscal',nota)



    def criar_segunda_janela(self):
        Segunda_janela(self, self.control)

    def criar_terceira_janela(self):
        Terceira_janela(self, self.control)

    def criar_quarta_janela(self):
        Quarta_janela(self, self.control)

    def criar_quinta_janela(self, carro):
        Quinta_janela(self, self.control, carro)



