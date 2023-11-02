valores_n = []
for i in range(20):
    n = int(input(f"Digite o valor de n {i + 1}: "))
    valores_n.append(n)

for n in valores_n:
    print(f"Tabuada de {n}:")
    for i in range(1, n + 1):
        resultado = i * n
        print(f"{i} x {n} = {resultado}")
   
