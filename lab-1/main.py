from bolo import Bolo 


def main ():
    boloDeCenouraComCobertura = Bolo("boloDeCenouraComCobertura", "chocolate", "cenoura", True)
    boloDeMorangoSemCobertura = Bolo("boloDeMorangoComCobertura", "morango", "branca", False)

    boloDeCenouraSemCobertura2 = boloDeCenouraComCobertura
    boloDeCenouraSemCobertura2.temCorbetura = False

    print("boloDeCenouraComCobertura tem corbetura? " + str(boloDeCenouraComCobertura.temCorbetura))
    print("boloDeMorangoSemCobertura tem corbetura? " + str(boloDeMorangoSemCobertura.temCorbetura))
    print("boloDeCenouraSemCobertura2 tem corbetura? " + str(boloDeCenouraSemCobertura2.temCorbetura))


main()



    