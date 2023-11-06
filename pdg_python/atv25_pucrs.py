total_preco_custo = 0
total_preco_novo = 0
contador_produtos = 0

while True:
    codigo = int(input("Digite o código do produto (ou um código negativo para encerrar): "))
    
    if codigo < 0:
        break
    
    preco_custo = float(input("Digite o preço de custo do produto: R$"))
    
    preco_novo = preco_custo * 1.2
    
    total_preco_custo += preco_custo
    total_preco_novo += preco_novo
    contador_produtos += 1
    
    print(f"Código do produto: {codigo}")
    print(f"Preço novo do produto: R${preco_novo:.2f}")
    print()


if contador_produtos > 0:
    media_preco_custo = total_preco_custo / contador_produtos
    media_preco_novo = total_preco_novo / contador_produtos
else:
    media_preco_custo = 0
    media_preco_novo = 0

print("Médias:")
print(f"Média dos preços de custo: R${media_preco_custo:.2f}")
print(f"Média dos preços com aumento: R${media_preco_novo:.2f}")
