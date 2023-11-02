while True:
    codigo_aluno = int(input("Digite o código do aluno: "))
    
    if codigo_aluno < 0:
        break 
    
    nota1 = float(input("Digite a primeira nota do aluno: "))
    nota2 = float(input("Digite a segunda nota do aluno: "))
    nota3 = float(input("Digite a terceira nota do aluno: "))
    
    maior_nota = max(nota1, nota2, nota3)
    media_ponderada = (4 * maior_nota + 3 * (nota1 + nota2 + nota3 - maior_nota)) / 10
    
    print(f"Código do aluno: {codigo_aluno}")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Média ponderada: {media_ponderada}")
    
    if media_ponderada >= 5:
        print("APROVADO")
    else:
        print("REPROVADO")
