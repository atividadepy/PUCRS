produtorio_pares = 1

while True:
    numero = int(input("Digite um número inteiro positivo (ou 0 para encerrar): "))
    
    if numero == 0:
        break
    
    if numero > 0 and numero % 2 == 0:
        produtorio_pares *= numero

if produtorio_pares == 1:
    print("Nenhum número par foi inserido.")
else:
    print(f"O produtório dos números pares é: {produtorio_pares}")
