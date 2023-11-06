soma = 0  
contagem = 0  

for numero in range(13, 74):  
    soma += numero
    contagem += 1

if contagem > 0:
    media = soma / contagem
    print(f"A média aritmética dos números entre 13 e 73 é: {media:.2f}")
else:
    print("Não há números no intervalo para calcular a média.")
