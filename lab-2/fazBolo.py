class FazBolo: 
    def __init__(self, massa: str, recheio: str, cobertura: str):
        self.massa = massa
        self.recheio = recheio
        self.cobertura = cobertura
    
    def assar(self):
        while True:
            temperatura = input("Insira a temperatura (fogo baixo, medio ou alto): ")

            # Valida se a temperatura é um dos três valores esperados pelo sistema. Se não, reincia o loop.
            if not (temperatura == "fogo alto" or temperatura == "fogo medio" or temperatura == "fogo baixo"):
                print("Temperatura inválida. Use: fogo baixo, fogo medio ou fogo alto.")
                continue
            
            # Valida se o tempo inserido é um inteiro não negativo. Se não, reincia o loop.
            try:
                tempo = int(input("Insira o tempo que vai deixar o bolo assando (em minutos): "))
                if tempo < 0:
                    print("Não dá pra desassar o bolo 😅.")
                    continue
            except ValueError:
                print("O tempo deve ser um número inteiro.")
                continue

            # Se todos os parâmetros estiverem certos, avalia o bolo. 
            print(f"\nVocê quer assar um bolo de massa {self.massa}, recheio {self.recheio}, cobertura {self.cobertura}, no {temperatura} por {tempo} minutos.")
            # Avalia se o bolo ficará cru, bom ou queimado
            print(self.avaliarBolo(temperatura, tempo))

    def avaliarBolo(self, temperatura: str, tempo: int):
        temposIdeais = {
            "fogo alto": 10,
            "fogo medio": 35,
            "fogo baixo": 45
        }

        if tempo > temposIdeais[temperatura]:
            return "Seu bolo vai queimar."
        elif tempo < temposIdeais[temperatura]:
            return "Seu bolo vai ficar cru."
        return "Me chama pro café."



        
