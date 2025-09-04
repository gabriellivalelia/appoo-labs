from aluno import Aluno

class Prova:
    def __init__(self):
        self.disciplina = input("Insira a disciplina da prova: ")
        self.dificuldade = self.setDificuldade()

    def setDificuldade(self):
        while True:
            try:
                value =  int(input("Insira a dificuldade da prova de 1 a 5: "))
                if(value < 1 or value > 5):
                    print("Por favor, insira um número de 1 a 5.")
                else: 
                    return value
            except ValueError:
                print("Por favor, insira um número.")
    
    def avisarProvaParaAluno(self, aluno: Aluno):
        estudoNecessario, reacao = aluno.reagirAProva(self.dificuldade)

        print(f"Ao saber da prova, a mais honesta reação do(a) aluno(a) {aluno.nome}, com matrícula {aluno.matricula} foi {reacao} pois sabia que precisaria de {estudoNecessario} para a prova de dificuldade {self.dificuldade} de {self.disciplina}")

