from tkinter import *
from tkinter import messagebox
from venda import Venda


class Quinta_janela(Toplevel):
    def __init__(self, parent, control, carro):
        super().__init__(parent)
        self.carro = carro
        self.control = control
        self.title(f'Venda - {self.carro.get_placa()}')
        self.geometry('400x200+200+200')
        self.transient(parent)
        self.grab_set()

        Label(self, text='').grid(row=0, column=0, padx=25, pady=5)
        Label(self, text='').grid(row=2, column=0, pady=5, padx=25)
        Label(self, text='').grid(row=0, column=2, padx=10)
        self.bt_canel = Button(self, text='Cancelar', width=10,
                               command=super().destroy).grid(row=4, column=1, pady=20)
        self.bt_confirm = Button(self, text='Confirmar', width=10,
                                 command=self.confirm_venda).grid(row=4, column=3, pady=20)

        self.cpf_comp_entry = StringVar()
        self.cpf_comp = Entry(self, textvariable=self.cpf_comp_entry).grid(row=1, column=3)
        self.cpf_comp_lbl = Label(self, text='CPF do Comprador').grid(row=1, column=1)

        self.mat_vend_entry = StringVar()
        self.mat_vend = Entry(self, textvariable=self.mat_vend_entry).grid(column=3, row=2)
        self.mat_vend_lbl = Label(self, text='Matrícula do Vendedor').grid(row=2, column=1)

        validation = self.register(self.only_numbers)
        self.preco_venda_entry = StringVar()
        self.preco_venda = Entry(self, validate='key', validatecommand=(validation, '%S'),
                                 textvariable=self.preco_venda_entry).grid(row=3, column=3)
        self.preco_venda_lbl = Label(self, text='Preço de Venda').grid(row=3, column=1)

    def confirm_venda(self):
        mat = self.mat_vend_entry.get()
        cpf = self.cpf_comp_entry.get()
        preco = float(self.preco_venda_entry.get())
        vend = None
        comp = None
        for v in self.control.bd.get_vendedor():
            if mat == v.get_matricula():
                vend = v
        for c in self.control.bd.get_comprador():
            if cpf == c.get_cpf():
                comp = c
        if vend is not None and comp is not None:
            venda = Venda(self.carro, vend, comp, preco)
            self.control.bd.add_venda(venda)
            self.control.bd.remover_carro(self.carro)
            self.control.jn.atualizar_patio()
            self.control.bd.save_carros()
            self.control.bd.save_vendas()
            self.gerar_nota(vend, comp, preco)
            super().destroy()
            nota = open('nota_fiscal.txt', 'r')
            messagebox.showinfo('Notal fiscal', nota.read())
        else:
            messagebox.showerror('Venda', 'Dados digitados incorretos. Por favor verificá-los.')

    def gerar_nota(self, vend, comp, preco):
        f = open('nota_fiscal.txt', 'w')
        f.write(f'''    Carro
Modelo: {self.carro.get_modelo()}
Marca: {self.carro.get_marca()}
Ano: {self.carro.get_ano()}
Estado {self.carro.get_estado()}
Placa: {self.carro.get_placa()}
Valor do Carro: {self.carro.get_preco()}
Valor recebido: {preco}
Cor: {self.carro.get_cor()}
    Comprador
Nome: {comp.get_nome()}
CPF: {comp.get_cpf()}

    Vendedor
Nome: {vend.get_nome()}
CPF: {vend.get_cpf()}
Matrícula: {vend.get_matricula()}''')
        f.close()

    def only_numbers(self, char):
        return char.isnumeric()