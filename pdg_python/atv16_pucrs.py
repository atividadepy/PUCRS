import math

contador_linhas = 0

print("Valor  |  Quadrado  |  Cubo  |  Raiz Quadrada")

while True:
    valor = float(input("Digite um valor (ou 0 para encerrar): "))

    if valor == 0:
        break 

    quadrado = valor ** 2
    cubo = valor ** 3
    raiz_quadrada = math.sqrt(valor)

    print(f"{valor}  |  {quadrado:.2f}  |  {cubo:.2f}  |  {raiz_quadrada:.2f}")

    contador_linhas += 1

    if contador_linhas % 20 == 0:
        print("Valor  |  Quadrado  |  Cubo  |  Raiz Quadrada")
