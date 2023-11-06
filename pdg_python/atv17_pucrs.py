while True:
    m = int(input("Digite o valor de m (ou um valor negativo para encerrar): "))
    if m < 0:
        break
    n = int(input("Digite o valor de n: "))
    
    soma = 0
    for i in range(n):
        soma += m + i
    
    print(f"A soma dos {n} inteiros consecutivos a partir de {m} é: {soma}")
