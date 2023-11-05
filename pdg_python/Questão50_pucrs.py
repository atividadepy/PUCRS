# Solicite ao usuário que digite os valores inteiros X e Y
x = int(input("Digite o valor de X (base): "))
y = int(input("Digite o valor de Y (expoente): "))

# Calcule a potência de X elevado a Y usando a função pow
resultado = pow(x, y)

print(f"{x}^{y} = {resultado}")
