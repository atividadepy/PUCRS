sexo = []
cor_olhos = []
cor_cabelos = []
idade = []

while True:
    print("Coleta de Dados de Habitante:")
    
    s = input("Sexo (M/F): ")
    olhos = input("Cor dos olhos (azuis/verdes/castanhos): ")
    cabelos = input("Cor dos cabelos (loiros/castanhos/pretos): ")
    age = int(input("Idade: "))
    

    sexo.append(s)
    cor_olhos.append(olhos)
    cor_cabelos.append(cabelos)
    idade.append(age)
    
    continuar = input("Deseja continuar a coleta de dados (S/N)? ").strip().lower()
    if continuar != 's':
        break


print("\nDados Coletados:")
for i in range(len(sexo)):
    print(f"Habitante {i + 1}:")
    print(f"Sexo: {sexo[i]}")
    print(f"Cor dos Olhos: {cor_olhos[i]}")
    print(f"Cor dos Cabelos: {cor_cabelos[i]}")
    print(f"Idade: {idade[i]} anos")
    print()


