from cliente import Cliente
from hotel import Hotel

def main():
    while(True):

        cliente = Cliente("Gabrielli")
        hotel = Hotel("China Park")

        contaDoCliente =  hotel.determineContaCliente(cliente)

        print(f"O cliente {cliente.nome} que ficou {cliente.diasEstadia} dias no hotel {hotel.nomeHotel} e consumiu ao todo {cliente.consumoRestaurante} refeições teve a conta de R${contaDoCliente}")

main()