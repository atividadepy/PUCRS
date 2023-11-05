# Dados das cidades (exemplo)
dados_cidades = [
    {
        'codigo': 1,
        'estado': 'RS',
        'veiculos': 1000,
        'acidentes': 10,
    },
    {
        'codigo': 2,
        'estado': 'SC',
        'veiculos': 1200,
        'acidentes': 8,
    },
    # Adicione os dados das outras cidades aqui...
]

# a) Encontrar o maior e o menor índice de acidentes de trânsito e suas cidades
acidentes_por_cidade = [(cidade['acidentes'], cidade['codigo']) for cidade in dados_cidades]
maior_indice = max(acidentes_por_cidade)
menor_indice = min(acidentes_por_cidade)

print(f"A cidade com maior índice de acidentes é a cidade {maior_indice[1]} com {maior_indice[0]} acidentes.")
print(f"A cidade com menor índice de acidentes é a cidade {menor_indice[1]} com {menor_indice[0]} acidentes.")

# b) Calcular a média de veículos nas cidades brasileiras
veiculos_totais = sum(cidade['veiculos'] for cidade in dados_cidades)
media_veiculos = veiculos_totais / len(dados_cidades)
print(f"A média de veículos nas cidades brasileiras é {media_veiculos:.2f} veículos por cidade.")

# c) Calcular a média de acidentes com vítimas nas cidades do Rio Grande do Sul
cidades_rs = [cidade for cidade in dados_cidades if cidade['estado'] == 'RS']
acidentes_rs = sum(cidade['acidentes'] for cidade in cidades_rs)
media_acidentes_rs = acidentes_rs / len(cidades_rs)
print(f"A média de acidentes com vítimas nas cidades do Rio Grande do Sul é {media_acidentes_rs:.2f}.")
