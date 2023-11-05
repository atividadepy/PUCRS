# Inicialize variáveis para armazenar o bônus
clientes = 150

for i in range(clientes):
    nome = input("Digite o nome do cliente: ")
    compras = float(input("Digite o valor das compras no ano passado: "))

    if compras < 500000:
        bonus = compras * 0.10
    else:
        bonus = compras * 0.15

    print(f"Cliente: {nome}, Bônus: R${bonus:.2f}")
