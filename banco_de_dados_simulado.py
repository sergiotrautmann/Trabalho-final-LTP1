from model import Carro
from model import Vendedor
from model import Comprador
from venda import Venda


class Bd_Simulado:
    def __init__(self):
        self.carros = []
        self.vendedor = []
        self.comprador = []
        self.vendas = []

    def carregar_carros(self):
        file = open('Carros.txt', 'r')
        for c in file.readlines():
            c = c.strip().lstrip('(').rstrip(')').split(',')
            carro = Carro(c[0].strip().strip('"').strip("'"),
                            c[1].strip().strip('"').strip("'"),
                            c[2].strip().strip('"').strip("'"),
                            c[3].strip().strip('"').strip("'"),
                            float(c[4].strip().strip('"').strip("'")),
                            c[5].strip().strip('"').strip("'"))
            self.carros.append(carro)
        file.close()

    def car_vendedores(self):
        file = open('vendedores.txt', 'r')
        for c in file.readlines():
            c = c.strip().lstrip('(').rstrip(')').split(',')
            vend = Vendedor(c[0].strip().strip('"').strip("'"),c[1].strip().strip('"').strip("'"),c[2].strip().strip('"').strip("'"))
            self.vendedor.append(vend)
        file.close()

    def car_compradores(self):
        file = open('compradores.txt', 'r')
        for c in file.readlines():
            c = c.strip().lstrip('(').rstrip(')').split(',')
            comp = Comprador(c[0].strip().strip('"').strip("'"),c[1].strip().strip('"').strip("'"))
            self.comprador.append(comp)
        file.close()

    def carregar_vendas(self):
        file = open('venda.txt', 'r')
        for c in file.readlines():
            c = c.strip().lstrip('((').rstrip(')').split(',')
            carro = Carro(c[0].strip().strip('"').strip("'"),c[1].strip().strip('"').strip("'"),c[2].strip().strip('"').strip("'"),c[3].strip().strip('"').strip("'"),c[4].strip().strip('"').strip("'"),c[5].strip().strip('),').strip("'").strip('"'))

            vend = Vendedor(c[6].strip().strip('(').strip('"').strip("'"),c[7].strip().strip('"').strip("'"),c[8].strip().strip('),').strip("'").strip('"'))

            comp = Comprador(c[9].strip().strip('(').strip('"').strip("'"),c[10].strip().strip('),').strip("'").strip('"'))

            preco = float(c[11])

            venda = Venda(carro, vend, comp, preco)

            self.vendas.append(venda)
        file.close()

    def add_carro(self, carro):
        self.carros.append(carro)

    def add_vendedor(self, vendedor):
        self.vendedor.append(vendedor)

    def add_comprador(self, comprador):
        self.comprador.append(comprador)

    def add_venda(self, venda):
        self.vendas.append(venda)

    def save_carros(self):
        file = open('carros.txt', 'w')
        for c in self.carros:
            file.write(str(c.get_dados()))
            file.write('\n')
        file.close()

    def save_vendedor(self):
        file = open('vendedores.txt', 'w')
        for c in self.vendedor:
            file.write(str(c.get_dados()))
            file.write('\n')
        file.close()

    def save_comprador(self):
        file = open('compradores.txt', 'w')
        for c in self.comprador:
            file.write(str(c.get_dados()))
            file.write('\n')
        file.close()

    def save_vendas(self):
        file = open('venda.txt', 'w')
        for c in self.vendas:
            file.write(str(c.info_venda()))
            file.write('\n')
        file.close()

    def get_carros(self):
        return self.carros

    def get_vendedor(self):
        return self.vendedor

    def get_comprador(self):
        return self.comprador

    def remover_vendedor(self, v):
        rmvd = v
        self.vendedor.remove(v)
        return rmvd

    def remover_comprador(self, c):
        rmvd = c
        self.comprador.remove(c)
        return rmvd

    def remover_carro(self, c):
        rmvd = c
        self.carros.remove(c)
        return rmvd
