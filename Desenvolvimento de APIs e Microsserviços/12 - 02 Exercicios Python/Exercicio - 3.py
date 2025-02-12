salario = float(input("Insira o quanto você recebe por hora: "))

horas =int(input("Insira quantas horas você trabalha por mês: "))

salarioBruto = (salario*horas)

inss = (salarioBruto/100) * 8
sindicato = (salarioBruto/100) * 5
parteDoLeao = (salarioBruto/100) * 11

salarioLiquido = salarioBruto - inss - sindicato - parteDoLeao

print("Você trabalha por:", horas," horas por mês")
print("Você recebe:", salario,"R$ por hora")
print("Você recebe:", salarioBruto,"R$ por mês")

print("Você paga 8% ao INSS o que representa:", inss,"R$ do seu salario")
print("Você paga 5% ao sindicato o que representa:", sindicato,"R$ do seu salario")
print("Você paga 11% de imposto de renda o que representa:", parteDoLeao,"R$ do seu salario")

salarioCalc = salarioBruto - inss
print(salarioCalc + inss,"-",inss, "=",salarioCalc)

salarioCalc = salarioCalc - sindicato
print(salarioCalc + sindicato,"-",sindicato, "=",salarioCalc)

salarioCalc = salarioCalc  - parteDoLeao
print(salarioCalc + parteDoLeao,"-",parteDoLeao, "=",salarioCalc)

print("Você recebe como salário final: ", salarioLiquido,"R$")
