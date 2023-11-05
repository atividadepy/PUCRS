a = [float(input("Digite um número: ")) for _ in range(5)]
negativos = len([num for num in a if num < 0])
print(f"Quantidade de números negativos: {negativos}")