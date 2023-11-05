def calcular_media_ponderada(n1, n2, n3):
    return (n1 * 2 + n2 * 4 + n3 * 3) / 10

def main():
    numero_alunos = 50
    notas_alunos = []

    for aluno in range(numero_alunos):
        print(f"Aluno {aluno + 1}")
        n1 = float(input("Digite a primeira nota: "))
        n2 = float(input("Digite a segunda nota: "))
        n3 = float(input("Digite a terceira nota: "))

        media_aluno = calcular_media_ponderada(n1, n2, n3)
        notas_alunos.append(media_aluno)

        if media_aluno >= 7:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado"

        print(f"Média do Aluno {aluno + 1}: {media_aluno:.2f} - {situacao}\n")

    media_geral = sum(notas_alunos) / numero_alunos
    print(f"Média Geral da Turma: {media_geral:.2f}")

if __name__ == "__main__":
    main()
