# Solicite ao usuário que digite um número inteiro positivo
n = int(input("Digite um número inteiro positivo: "))

# Verifique se o número é positivo
if n < 0:
    print("O número deve ser positivo.")
else:
    fatorial = 1
    for i in range(1, n + 1):
        fatorial *= i

    print(f"{n}! = {fatorial}")
