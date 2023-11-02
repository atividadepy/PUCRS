def tabuada():
    N = int(input("Digite um valor para N: "))
    
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            resultado = i * j 
            print(f"{i} x {j} = {resultado}")
            
            
if __name__ == "__main__":
    tabuada()
    
    
def alunos_alturas():
    aluno_mais_alto = 0
    altura_aluno_mais_alto = 0
    aluno_mais_baixo = 0
    altura_aluno_mais_baixo = float('inf')
    
    for i in range(5):
        numero_aluno = int(input("Digite o número do aluno: "))
        altura = int(input("Digite a altura do aluno em centímetros: "))
        
        if altura > altura_aluno_mais_alto:
            aluno_mais_alto = numero_aluno
            altura_aluno_mais_alto = altura
            
            
        if altura < altura_aluno_mais_baixo:
            aluno_mais_baixo = numero_aluno
            altura_aluno_mais_baixo = altura
            
    print(f"Aluno mais alto: Número [aluno_mais_alto] - Altura: {altura_aluno_mais_alto} cm")
    print(f"Aluno mais baixo: Número [aluno_mas_baixo] - Altura: {altura_aluno_mais_baixo} cm")
    
    if __name__ == "__main__":
        alunos_alturas()
        
    