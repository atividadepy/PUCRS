# Inicialize as variáveis para armazenar os dados
total_idade = 0
total_altura_mulheres = 0
total_idade_homens = 0
pessoas_18_35 = 0
total_pessoas = 0

# Use um loop para ler os dados das 1000 pessoas
while total_pessoas < 1000:
    sexo = int(input("Digite o sexo (0-feminino, 1-masculino): "))
    idade = int(input("Digite a idade: "))
    altura = float(input("Digite a altura (em metros): "))

    total_idade += idade

    if sexo == 0:
        total_altura_mulheres += altura
    elif sexo == 1:
        total_idade_homens += idade

    if 18 <= idade <= 35:
        pessoas_18_35 += 1

    total_pessoas += 1

# Calcular as médias e o percentual
media_idade = total_idade / total_pessoas
media_altura_mulheres = total_altura_mulheres / total_pessoas
media_idade_homens = total_idade_homens / total_pessoas
percentual_18_35 = (pessoas_18_35 / total_pessoas) * 100

# Exibir os resultados
print(f"A média da idade do grupo é {media_idade:.2f} anos.")
print(f"A média da altura das mulheres é {media_altura_mulheres:.2f} metros.")
print(f"A média da idade dos homens é {media_idade_homens:.2f} anos.")
print(f"O percentual de pessoas com idade entre 18 e 35 anos é {percentual_18_35:.2f}%.")
