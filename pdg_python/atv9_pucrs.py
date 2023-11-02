maior_valor = float('-inf')  
menor_valor = float('inf')   

for x in range(50):
    valor = float(input(f"Digite o {x+1}º valor: "))
    
    if valor > maior_valor:
        maior_valor = valor
    
    if valor < menor_valor:
        menor_valor = valor

print(f"O maior valor é: {maior_valor}")
print(f"O menor valor é: {menor_valor}")
