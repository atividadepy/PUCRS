n = int(input("Digite o número de termos da progressão aritmética: "))
a1 = float(input("Digite o primeiro termo da progressão: "))
r = float(input("Digite a razão da progressão: "))

soma_elementos = 0

print("Termos da progressão aritmética:")

for i in range(n):
    termo = a1 + i * r  #
    print(termo)
    soma_elementos += termo  

print(f"Soma dos elementos: {soma_elementos}")
