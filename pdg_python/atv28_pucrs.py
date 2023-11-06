n = int(input("Digite um valor inteiro e positivo (n): "))
S = 0.0

if n <= 0:
    print("O valor de n deve ser inteiro e positivo.")
else:
    for i in range(1, n + 1):
        termo = 1 / i
        S += termo
        print(f"Termo {i}: 1/{i} = {termo:.4f}")

    print(f"O valor final de S é: {S:.4f}")
