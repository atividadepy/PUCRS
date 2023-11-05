def calcular_somatorio(n):
    somatorio = 0
    for i in range(1, n + 1):
        somatorio += i
    return somatorio

def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, n + 1):
            fatorial *= i
        return fatorial

def main():
    n = int(input("Quantos valores deseja ler? "))
    
    print("Valor Lido | Somatório | Fatorial")
    for _ in range(n):
        m = int(input("Digite um valor inteiro e positivo: "))
        somatorio = calcular_somatorio(m)
        fatorial = calcular_fatorial(m)
        print(f"{m:^10} | {somatorio:^9} | {fatorial:^8}")

if __name__ == "__main__":
    main()
