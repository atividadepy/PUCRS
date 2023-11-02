def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

def main():
    N = int(input("Digite o número de valores que deseja ler: "))

    for i in range(N):
        valor = int(input(f"Digite o {i+1}º valor: "))
        resultado_fatorial = fatorial(valor)
        print(f"Valor lido: {valor}, Fatorial: {resultado_fatorial}")

if __name__ == "__main__":
    main()