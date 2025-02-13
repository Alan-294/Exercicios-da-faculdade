dataRuim = input("Digite uma data no formato DD/MM/AAAA: ")
dataArray = []
for i in dataRuim:
    dataArray.append(i)

dias = dataArray[0] + dataArray[1]
mes = dataArray[3]+dataArray[4]
ano = dataArray[6]+dataArray[7]+dataArray[8]+dataArray[9]

if mes == "01":
    mes = "janeiro"
if mes == "02":
    mes = "fevereiro"
if mes == "03":
    mes = "março"
if mes == "04":
    mes = "abril"
if mes == "05":
    mes = "maio"
if mes == "06":
    mes = "junho"
if mes == "07":
    mes = "julho"
if mes == "08":
    mes = "agosto"
if mes == "09":
    mes = "setembro"
if mes == "10":
    mes = "outubro"
if mes == "11":
    mes = "novembroo"
if mes == "12":
    mes = "dezembro"



print(dias,"de", mes,"de", ano)
