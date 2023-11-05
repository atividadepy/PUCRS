import math

N = int(input("Digite um número inteiro e positivo: "))
E = sum([1 / math.factorial(i) for i in range(N+1)])
print(f"O valor de E é: {E}")
