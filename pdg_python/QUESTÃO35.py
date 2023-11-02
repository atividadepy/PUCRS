def main():
    maior_altura = 0
    menor_altura = float('inf')
    total_altura_mulheres = 0
    total_altura_turma = 0
    total_mulheres = 0

    for i in range(50):
        altura = float(input("Digite a altura da pessoa: "))
        sexo = int(input("Digite o sexo da pessoa (1 para masculino, 2 para feminino): "))

        if altura > maior_altura:
            maior_altura = altura

        if altura < menor_altura:
            menor_altura = altura

        total_altura_turma += altura

        if sexo == 2:  # Se for feminino
            total_altura_mulheres += altura
            total_mulheres += 1

    media_altura_mulheres = total_altura_mulheres / total_mulheres
    media_altura_turma = total_altura_turma / 50

    print("Maior altura da turma:", maior_altura)
    print("Menor altura da turma:", menor_altura)
    print("Média da altura das mulheres:", media_altura_mulheres)
    print("Média da altura da turma:", media_altura_turma)

if __name__ == "__main__":
    main()