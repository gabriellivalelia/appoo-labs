class Cliente: 
    def __init__(self, nome: str):
        self.nome = nome
        self.diasEstadia = self.setValor("Informe o número de dias que o cliente permaneceu no hotel: ")
        self.consumoRestaurante = self.setValor("Informe a quantidade total de refeições que o cliente consumiu: ")

    def fornecaValorConta(self, valorDiaria: float, valorRefeicao: float):
        return self.diasEstadia*valorDiaria + self.consumoRestaurante*valorRefeicao
    
    def setValor(self, msg: str):
        while True:
            try:
                value =  int(input(msg))
                if(value < 0):
                    print("Por favor, insira um número não negativo.")
                else: 
                    return value
            except ValueError:
                print("Por favor, insira um número inteiro válido.")


        
    