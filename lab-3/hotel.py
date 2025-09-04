from cliente import Cliente

class Hotel: 
    def __init__(self, nomeHotel: str):
        self.nomeHotel = nomeHotel
        self.valorDiaria = 100.00
        self.valorRefeicao = 50.00

    def determineContaCliente(self, cliente: Cliente):
        return cliente.fornecaValorConta(self.valorDiaria, self.valorRefeicao)

        
