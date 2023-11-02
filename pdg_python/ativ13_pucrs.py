# Função para calcular o fatorial de um número
def fatorial(numero):
    if numero == 0:
        return 1
    else:
        fat = 1
        for i in range(1, numero + 1):
            fat *= i
        return fat
    
n = int(input("Digite o número de valores a serem lidos: "))

for i in range(n):
    valor = int(input(f"Digite o {i + 1}º valor: "))
    resultado_fatorial = fatorial(valor)
    print(f"Valor: {valor}, Fatorial: {resultado_fatorial}")
