fim = int(input("Insira até que elemento de Fibonacci você quer ver: "))
cont = 1
fibo =[1, 1]
while cont <= fim:
    fibo.append(fibo[cont] + fibo[cont - 1])
    cont = cont + 1
    
print(fibo)