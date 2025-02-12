nome = input("Olá, digite o seu nome: ")
nota1 = float(input("Digite a sua nota na AP1:"))
nota2 = float(input("Digite a sua nota na AP2:"))

media = (nota1 + nota2) /2
print("(",nota1,"+",nota2,") / 2 =",media)

if media == 10:
    print("Parabéns ",nome,"a sua média foi", media, "o que significa que você foi Aprovado com Distinção")

elif media < 10 and media >= 7:
    print("Parabéns ",nome,"a sua média foi", media, "o que significa que você foi Aprovado")

elif media < 7 and media >= 0:
    print("Infelizmente ",nome,"a sua média foi", media, "o que significa que você foi Reprovado")
    
else:
    print("Erro no sistema, foi digitado um valor inválido nas notas")

    