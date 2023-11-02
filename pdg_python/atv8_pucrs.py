soma_pares = 0
contador_pares = 0

while True:
    numero = int(input("Digite um número (ou 0 para encerrar): "))

    if numero == 0:
        break  
    elif numero % 2 == 0:
        soma_pares += numero
        contador_pares += 1

if contador_pares > 0:
    media_pares = soma_pares / contador_pares
    print(f"A média dos números pares inseridos é: {media_pares}")
else:
    print("Nenhum número par foi inserido.")

