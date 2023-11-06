import math

while True:
    m = int(input("Digite um valor inteiro e positivo (ou um valor negativo para encerrar): "))
    if m < 0:
        break
    
    if m % 2 == 0:  
        divisores = [i for i in range(1, m + 1) if m % i == 0]
        print(f"{m} é um número par e possui {len(divisores)} divisores: {divisores}")
    elif m < 10:  
        fatorial = math.factorial(m)
        print(f"O fatorial de {m} é {fatorial}")
    else:  
        soma = sum(range(1, m + 1))
        print(f"A soma dos inteiros de 1 até {m} é {soma}")
