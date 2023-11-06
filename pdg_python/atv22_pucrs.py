soma_salarios = 0
quantidade_habitantes = 0
maior_idade = -1
menor_idade = float('inf')
mulheres_salario_ate_100 = 0

while True:
    idade = int(input("Digite a idade (ou um número negativo para encerrar): "))
    
    if idade < 0:
        break
    
    sexo = input("Digite o sexo (M/F): ")
    salario = float(input("Digite o salário: R$"))
    

    soma_salarios += salario
    quantidade_habitantes += 1
    

    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade:
        menor_idade = idade
    

    if sexo.upper() == 'F' and salario <= 100:
        mulheres_salario_ate_100 += 1


if quantidade_habitantes > 0:
    media_salario = soma_salarios / quantidade_habitantes
else:
    media_salario = 0


print(f"A média de salário do grupo é: R${media_salario:.2f}")
print(f"Maior idade do grupo: {maior_idade} anos")
print(f"Menor idade do grupo: {menor_idade} anos")
print(f"Quantidade de mulheres com salário até R$100,00: {mulheres_salario_ate_100}")
