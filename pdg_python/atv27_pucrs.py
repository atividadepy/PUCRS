maior_valor = float('-inf')
menor_valor = float('inf')
soma_valores = 0

for _ in range(500):
    valor = int(input("Digite um valor inteiro e positivo: "))
    
    if valor < 0:
        print("Valor negativo inserido. Por favor, insira apenas valores inteiros e positivos.")
        continue

    if valor > maior_valor:
        maior_valor = valor

    if valor < menor_valor:
        menor_valor = valor

    soma_valores += valor

media_valores = soma_valores / 500

print(f"O maior valor é: {maior_valor}")
print(f"O menor valor é: {menor_valor}")
print(f"A média dos valores é: {media_valores:.2f}")
