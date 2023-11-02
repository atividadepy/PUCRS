soma_notas = 0
contador_alunos = 0

while True:
    codigo_aluno = int(input("Digite o código do aluno (ou 0 para encerrar): "))
    
    if codigo_aluno >= 30:
        print("Código inválido")
    elif codigo_aluno >= 1 and codigo_aluno <=3:

        nota1 = float(input("Digite a primeira nota do aluno: "))
        nota2 = float(input("Digite a segunda nota do aluno: "))
        nota3 = float(input("Digite a terceira nota do aluno: "))
        
        media_aluno = (nota1 + nota2 + nota3) / 3
        print(f"A média do aluno de código {codigo_aluno} é: {media_aluno}")
        
        soma_notas += media_aluno
        contador_alunos += 1

if contador_alunos > 0:
    media_classe = soma_notas / contador_alunos
    print(f"A média da classe é: {media_classe}")
else:
    print("Nenhum aluno foi inserido.")
