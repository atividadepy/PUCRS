# Inicialize uma lista vazia para armazenar os grupos de valores
grupos = []

# Leia os 5 grupos de 4 valores
for i in range(5):
    grupo = []
    for j in range(4):
        valor = int(input(f"Digite o valor {j + 1} do grupo {i + 1}: "))
        grupo.append(valor)
    grupos.append(grupo)

# Mostre os grupos na ordem lida
print("Grupos na ordem lida:")
for grupo in grupos:
    print(grupo)

# Ordene os grupos em ordem decrescente
grupos_ordenados = sorted(grupos, reverse=True)

# Mostre os grupos ordenados em ordem decrescente
print("Grupos ordenados em ordem decrescente:")
for grupo in grupos_ordenados:
    print(grupo)
