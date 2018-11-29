from tkinter import *
from model import Carro
from tkinter import messagebox


class Segunda_janela(Toplevel):
    def __init__(self, parent, control):
        super().__init__(parent)
        self.control = control
        self.title('Carros')
        self.geometry('400x400+200+200')
        self.transient(parent)
        self.grab_set()

        Label(self, text='').grid(row=0, column=2, padx=20, pady=2)
        Label(self, text='').grid(row=0, column=0, padx=20, pady=2)
        Label(self, text='').grid(row=47, column=0, padx=20, pady=20)

        self.btn_add = Button(self, text='Adicionar', command=self.add_car).grid(row=10, column=1, columnspan=3, pady=10, stick=S)
        self.bt_rmv = Button(self, text='Remover', command=self.rmv_car).grid(row=49, column=1, columnspan=3, pady=10, stick=S)

        self.btn_close = Button(self, text='Fechar Janela', command=self.destroy, width=10)
        self.btn_close.grid(row=50, column=1, columnspan=3, stick=S, pady=20)

        self.entry_mod_var = StringVar()
        self.entry_mod = Entry(self, textvariable=self.entry_mod_var).grid(row=1, column=3)
        self.lbl_mod = Label(self, text='Modelo').grid(row=1, column=1, stick=E)

        self.entry_marca_var = StringVar()
        self.entry_marca = Entry(self, textvariable=self.entry_marca_var).grid(row=2, column=3)
        self.lbl_mod = Label(self, text='Marca').grid(row=2, column=1, stick=E)

        self.entry_ano_var = StringVar()
        self.entry_ano = Entry(self, textvariable=self.entry_ano_var).grid(row=3, column=3)
        self.lbl_ano = Label(self, text='Ano').grid(row=3, column=1, stick=E)

        validation = self.register(self.only_numbers)
        self.entry_preco_var = StringVar()
        self.entry_preco = Entry(self, validate='key', validatecommand=(validation, '%S'),
                                 textvariable=self.entry_preco_var).\
            grid(row=4, column=3)
        self.lbl_preco = Label(self, text='Preço de Compra').\
            grid(row=4, column=1, stick=E)

        self.entry_estado_var = StringVar()
        self.entry_estado = Entry(self, textvariable=self.entry_estado_var).\
            grid(row=5, column=3)
        self.lbl_estado = Label(self, text='Estado').\
            grid(row=5, column=1, stick=E)

        self.entry_placa_var = StringVar()
        self.entry_placa = Entry(self, textvariable=self.entry_placa_var).\
            grid(row=6, column=3)
        self.lbl_placa = Label(self, text='Placa').\
            grid(row=6, column=1, stick=E)

        self.entry_placa_var2 = StringVar()
        self.entry_placa2 = Entry(self, textvariable=self.entry_placa_var2). \
            grid(row=48, column=3)
        self.lbl_placa2 = Label(self, text='Placa'). \
            grid(row=48, column=1, stick=E)
        self.entry_cor_var = StringVar()
        self.entry_cor = Entry(self, textvariable=self.entry_cor_var).grid(row=7, column=3)
        self.lbl_cor = Label(self, text='Cor').grid(row=7, column=1, stick=E)
    def add_car(self):
        modelo = self.entry_mod_var.get()
        marca = self.entry_marca_var.get()
        ano = self.entry_ano_var.get()
        preco = float(self.entry_preco_var.get())
        estado = self.entry_estado_var.get()
        placa = self.entry_placa_var.get()
        cor = self.entry_cor_var.get()
        c = Carro(modelo, marca, ano, estado, preco, placa, cor)
        self.control.bd.add_carro(c)
        messagebox.showinfo('Carro', f'{placa} foi adicionado.')

    def rmv_car(self):
        placa = self.entry_placa_var2.get()
        rmvd = None
        if messagebox.askyesno('Excluir', f'Tem ceteza que deseja excluir o carro: {placa}?') is False:
            return None
        for c in self.control.bd.get_carros():
            if c.get_placa() == placa:
                rmvd = self.control.bd.remover_carro(c)
                messagebox.showinfo('Carro', f'{placa} foi removido.')
        if rmvd is None:
            messagebox.showerror('Carro', 'Não há carro cadastrado com estes dados.')

    def destroy(self):
        self.control.bd.save_carros()
        self.control.jn.atualizar_patio()
        super().destroy()

    def only_numbers(self, char):
        return char.isnumeric()