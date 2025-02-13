from jogo import Jogao

print("Vamos jogar Craps!")
cont = 1

print("Jogada número",cont)

jogada = Jogao()

jogar = input("Aperte qualquer caractere e aperte enter para jogar o primeiro dado: ")
print("Os seus dados sairam: ")
print(jogada.jogar_dados())
jogada.primJogada()

cont = cont + 1
while True:
    if jogada.vitoria == True:
        break
    print("Jogada número",cont)
    jogar = input("Aperte qualquer caractere e aperte enter para jogar dados: ")

    print("A soma dos seus dados saiu:", jogada.jogar_dados())
    jogada.jogada()

    cont = cont + 1

print("O resultado de todas as suas jogadas foram:",jogada.jogadas)