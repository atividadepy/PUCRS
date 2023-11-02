
soma = 0
contador = 0
positivos = 0
negativos = 0

while True:
    valor = float(input("Digite um valor (ou 0 para encerrar): "))
    
    if valor == 0:
        break  
    else:
        soma += valor
        contador += 1
        if valor > 0:
            positivos += 1
        elif valor < 0:
            negativos += 1


if contador > 0:
    media = soma / contador
    percentual_positivos = (positivos / contador) * 100
    percentual_negativos = (negativos / contador) * 100
    
    print(f"Média dos valores: {media}")
    print(f"Quantidade de valores positivos: {positivos}")
    print(f"Quantidade de valores negativos: {negativos}")
    print(f"Percentual de valores positivos: {percentual_positivos}%")
    print(f"Percentual de valores negativos: {percentual_negativos}%")
else:
    print("Nenhum valor foi inserido.")
