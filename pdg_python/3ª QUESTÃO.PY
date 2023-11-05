salarios = []
filhos = []

while True:
    salario = float(input("Digite o salário: "))
    if salario < 0:
        break
    salarios.append(salario)
    filhos.append(int(input("Digite o número de filhos: ")))

media_salario = sum(salarios) / len(salarios)
media_filhos = sum(filhos) / len(filhos)
maior_salario = max(salarios)
perc_ate_100 = len([s for s in salarios if s <= 100]) / len(salarios) * 100

print(f"Média do salário: {media_salario}")
print(f"Média do número de filhos: {media_filhos}")
print(f"Maior salário: {maior_salario}")
print(f"Percentual de pessoas com salário até R$100,00: {perc_ate_100}%")