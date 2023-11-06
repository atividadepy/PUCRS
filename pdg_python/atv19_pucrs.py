total_numeros = 0
soma_numeros = 0
numeros_pares = 0
soma_pares = 0

while True:
    numero = int(input("Digite um número (ou 0 para encerrar): "))
    
    if numero == 0:
        break
    
    total_numeros += 1
    soma_numeros += numero
    
    if numero % 2 == 0:
        numeros_pares += 1
        soma_pares += numero

if total_numeros == 0:
    print("Nenhum número positivo foi inserido.")
else:
    numeros_impares = total_numeros - numeros_pares
    media_geral = soma_numeros / total_numeros
    
    if numeros_pares > 0:
        media_pares = soma_pares / numeros_pares
        print(f"Quantidade de números pares: {numeros_pares}")
        print(f"Média de valores pares: {media_pares:.2f}")
    
    print(f"Quantidade de números ímpares: {numeros_impares}")
    print(f"Média geral dos números lidos: {media_geral:.2f}")
