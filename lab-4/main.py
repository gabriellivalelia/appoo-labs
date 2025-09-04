from aluno import Aluno
from prova import Prova

def main():
    aluno = Aluno("Gabrielli", "2022055513")
    prova = Prova()

    prova.avisarProvaParaAluno(aluno)


main()