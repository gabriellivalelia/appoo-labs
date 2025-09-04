class Aluno: 
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def reagirAProva(self, dificuldadeDaProva: int):
        estudoNecessario = ""
        reacao = ""
        
        if dificuldadeDaProva == 1:
            estudoNecessario = "Metade senso comum e metade malemolejo"
            reacao = "(^⁻^)"
        elif dificuldadeDaProva == 2:
            estudoNecessario = "Uma lida nos slides"
            reacao = "(o_o)"
        elif dificuldadeDaProva == 3:
            estudoNecessario = "Fazer os exercicios pares"
            reacao = "(O_O)"
        elif dificuldadeDaProva == 4:
            estudoNecessario = "Jantar o livro à milanesa"
            reacao = "(T_T)"
        elif dificuldadeDaProva == 5:
            estudoNecessario = "Torcer para um milagre"
            reacao = " (╯°□°）╯︵ ┻━┻"
        
        return estudoNecessario, reacao
    
