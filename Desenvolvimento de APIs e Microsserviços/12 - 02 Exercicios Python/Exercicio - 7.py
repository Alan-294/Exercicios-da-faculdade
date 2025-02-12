eleitores = int(input("Insira o número de eleitores: "))
cont = 1
candidato1 = 0
candidato2 = 0
candidato3 = 0

print("Prefeito de Sorocaba: 1")
print("Marcio Anti corrupção: 2")
print("Chapolim Colorado: 3")


while cont <= eleitores:
    print("Voto número ",cont, "°")
    voto = int(input("Digite o número do candidato em que você vai votar: "))
    if voto == 1:
        candidato1 = candidato1 + 1
    
    if voto == 2:
        candidato2 = candidato2 + 1
        
    if voto == 3:
        candidato3 = candidato3 + 1
    cont = cont + 1
    
print("Houveram",eleitores," eleitores, no fim a votação foi:")
print("Prefeito de Sorocaba:",candidato1)  
print("Marcio Anti corrupção:",candidato2)
print("Chapolim Colorado:",candidato3)


if candidato1 > candidato2 and candidato1 > candidato3:
    print("O ganhador foi o Prefeiro de Sorocaba")
    

if candidato2 > candidato1 and candidato2 > candidato3:
    print("O ganhador foi o Marcio Anti corrupção")
    

if candidato3 > candidato2 and candidato3 > candidato1:
    print("O ganhador foi o Chapolim Colorado")