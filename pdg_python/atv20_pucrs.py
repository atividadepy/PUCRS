soma_negativos = 0

while True:
    numero = int(input("Digite um número inteiro (ou 0 para encerrar): "))
    
    if numero == 0:
        break
    
    if numero < 0:
        soma_negativos += numero

print(f"O somatório dos números negativos é: {soma_negativos}")
