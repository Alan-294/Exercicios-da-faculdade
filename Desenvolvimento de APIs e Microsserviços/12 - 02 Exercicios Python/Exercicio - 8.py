import random
print("Vamos jogar Craps!")
jogadas = []
cont = 1
vitoria = False
print("Jogada número",cont)
jogar = input("Aperte qualquer caractere e aperte enter para jogar o primeiro dado: ")
num1 = random.randint(1, 6)
print("O seu primeiro dado saiu:", num1)
    
jogar = input("Aperte qualquer caractere e aperte enter para jogar o segundo dado: ")
num2 = random.randint(1, 6)
print("O seu segundo dado saiu:", num2)

resultado = num1 + num2
jogadas.append(resultado)
print("A soma dos seus dados saiu:",resultado)

if resultado == 7 or resultado == 11:
    print("Parabéns, você ganhou pois o seu resultado foi 7 ou 11 o que configura como vitória natural")
    vitoria = True
        
elif resultado == 2 or resultado == 3 or resultado == 12:
    print("Que pena, você perdeu pois o seu resultado foi 2, 3 ou 12 o que configura como derrota por craps")
    vitoria = True
        
else:
    print("Agora o valor que você tirou",resultado," vai ser o seu Ponto, você tera que lançar os dados novamente e vence se tirar o ponto denovo e perde se tirar um 7")
    ponto = resultado

cont = cont + 1
while True:
    if vitoria == True:
        break
    print("Jogada número",cont)
    jogar = input("Aperte qualquer caractere e aperte enter para jogar o primeiro dado: ")
    num1 = random.randint(1, 6)
    print("O seu primeiro dado saiu:", num1)
    
    jogar = input("Aperte qualquer caractere e aperte enter para jogar o segundo dado: ")
    num2 = random.randint(1, 6)
    print("O seu segundo dado saiu:", num2)
    
    resultado = num1 + num2
    jogadas.append(resultado)
    print("A soma dos seus dados saiu:",resultado)
    
    if resultado == ponto:
        print("Parabéns, você ganhou pois o seu resultado",resultado,"foi igual ao seu ponto")
        break
    if resultado == 7:
        print("Que pena, você perdeu pois o seu resultado foi 7 antes de tirar o ponto")
        break
    
print("O resultado de todas as suas jogadas foram:",jogadas)