votos_candidato = [1, 2, 3, 4] 
votos_nulos = 5
votos_branco = 6

while True:
    voto = int(input("Digite o código do seu candidato: "))

    if voto == 0:
        break 
    elif voto >= 1 and voto <= 4:
        votos_candidato[voto - 1] += 1  
    elif voto == 5:
        votos_nulos += 1
    elif voto == 6:
        votos_branco += 1
    else:
        print("Código de voto inválido. Por favor, digite um código válido.")


for i in range(4):
    print(f"Total de votos para o candidato {i + 1}: {votos_candidato[i]}")
print(f"Total de votos nulos: {votos_nulos}")
print(f"Total de votos em branco: {votos_branco}")
