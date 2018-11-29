class Venda:
    def __init__(self, carro, vend, comp, preco):
        self.carro = carro
        self.vendedor = vend
        self.comprador = comp
        self.preco = preco


    def info_venda(self):
        return self.carro.get_dados(), self.vendedor.get_dados(), self.comprador.get_dados(), self.preco