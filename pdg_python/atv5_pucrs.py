
soma = 0
contador = 0

while True:
    valor = int(input("Digite um valor inteiro positivo (ou um valor negativo para sair): "))
    
    if valor < 0:
        break  
    else:
        soma += valor
        contador += 1

if contador > 0:
    media = soma / contador
    print(f"A média dos valores inseridos é: {media}")
else:
    print("Nenhum valor positivo foi inserido.")
