# Inicialize as variáveis para armazenar as informações
maior_idade = 0
contagem_mulheres_verdes_louros = 0

# Loop para coletar informações das 500 pessoas
for i in range(500):
    sexo = input("Digite o sexo (M/F): ")
    idade = int(input("Digite a idade: "))
    olhos = input("Digite a cor dos olhos (A/V/C): ")
    cabelos = input("Digite a cor dos cabelos (L/C/P): ")

    # Verifique a maior idade
    if idade > maior_idade:
        maior_idade = idade

    # Verifique se é uma mulher com as características especificadas
    if sexo == "F" and 18 <= idade <= 35 and olhos == "V" and cabelos == "L":
        contagem_mulheres_verdes_louros += 1

print(f"A maior idade do grupo é {maior_idade} anos.")
print(f"A quantidade de mulheres com idade entre 18 e 35 anos, olhos verdes e cabelos louros é {contagem_mulheres_verdes_louros}.")
