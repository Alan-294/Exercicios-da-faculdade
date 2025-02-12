ano = int(input("Insira um ano: "))

if ano % 4 == 0 and ano % 100 != 0:
    print("O ano é Bissexto")
    
elif ano % 100 == 0 and ano % 400 == 0:
    print("O ano é Bissexto")
    
else:
    print("O ano não é Bissexto")