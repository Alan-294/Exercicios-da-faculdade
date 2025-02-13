import random

class Jogao:
    def __init__(self):
        self.jogadas = []
        self.vitoria = False
        self.resultado = 0
        self.ponto = 0

    def jogar_dados(self):
        self.num1 = random.randint(1, 6)
        self.num2 = random.randint(1, 6)

        self.jogadas.append(self.num1 + self.num2)
        self.resultado = self.num1+self.num2

        return self.num1, self.num2, 'o que resulta em',self.num1+self.num2
    
    def primJogada(self):

        if self.resultado == 7 or self.resultado == 11:
            print("Parabéns, você ganhou pois o seu resultado foi 7 ou 11 o que configura como vitória natural")
            self.vitoria = True
                
        elif self.resultado == 2 or self.resultado == 3 or self.resultado == 12:
            print("Que pena, você perdeu pois o seu resultado foi 2, 3 ou 12 o que configura como derrota por craps")
            self.vitoria = True
                
        else:
            print("Agora o valor que você tirou",self.resultado," vai ser o seu Ponto, você tera que lançar os dados novamente e vence se tirar o ponto denovo e perde se tirar um 7")
            self.ponto = self.resultado

              
    def jogada(self):
        if self.resultado == self.ponto:
            print("Parabéns, você ganhou pois o seu resultado", self.resultado,"foi igual ao seu ponto")
            self.vitoria = True
            return

        if self.resultado == 7:
            print("Que pena, você perdeu pois o seu resultado foi 7 antes de tirar o ponto")
            self.vitoria = True
            return
        return