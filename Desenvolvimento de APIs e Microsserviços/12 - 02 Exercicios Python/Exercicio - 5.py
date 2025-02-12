lista = []
cont = 1
pares = 0
impares = 0
while cont <= 10:
    print("Digite o",cont,"° número da lista: ")
    num = int(input())
    
    if num % 2 ==0:
        pares = pares + 1
    else:
        impares = impares + 1
        
    lista.append(num)
    cont = cont + 1

print(lista)
print("Números pares:",pares)
print("Números impares:",impares)
