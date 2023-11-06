maior_idade = 0
contagem_mulheres = 0

while True:
    idade = int(input("Digite a idade do habitante (ou -1 para encerrar): "))

    if idade == -1:
        break

    sexo = input("Digite o sexo do habitante (M/F): ").upper()
    cor_olhos = input("Digite a cor dos olhos do habitante (azuis/verdes/castanhos): ").lower()
    cor_cabelos = input("Digite a cor dos cabelos do habitante (loiros/castanhos/pretos): ").lower()

    if idade > maior_idade:
        maior_idade = idade

    if sexo == "F" and 18 <= idade <= 35 and cor_olhos == "verdes" and cor_cabelos == "louros":
        contagem_mulheres += 1

print(f"A maior idade dos habitantes é: {maior_idade} anos")

if contagem_mulheres > 0:
    print(f"Quantidade de mulheres com idade entre 18 e 35 anos, olhos verdes e cabelos loiros: {contagem_mulheres}")
else:
    print("Não há mulheres com essas características na amostra.")
