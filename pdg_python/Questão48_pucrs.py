# Inicialize uma lista para armazenar as informações dos alunos
alunos = []

# Loop para coletar as informações de cada aluno
for i in range(75):
    matricula = input("Digite o número de matrícula do aluno: ")
    nota = float(input("Digite a nota numérica final do aluno: "))
    
    if 0.0 <= nota <= 4.9:
        conceito = "D"
    elif 5.0 <= nota <= 6.9:
        conceito = "C"
    elif 7.0 <= nota <= 8.9:
        conceito = "B"
    elif 9.0 <= nota <= 10.0:
        conceito = "A"
    else:
        conceito = "Nota inválida"
    
    alunos.append((matricula, nota, conceito))

# Exibir os conceitos finais dos alunos
for aluno in alunos:
    matricula, nota, conceito = aluno
    print(f"Matrícula: {matricula}, Nota: {nota}, Conceito: {conceito}")
