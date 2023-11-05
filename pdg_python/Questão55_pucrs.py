from datetime import datetime

# Solicite ao usuário que digite as duas datas no formato 'dd/mm/aaaa'
data_str1 = input("Digite a primeira data (dd/mm/aaaa): ")
data_str2 = input("Digite a segunda data (dd/mm/aaaa): ")

# Converta as datas de strings para objetos datetime
data1 = datetime.strptime(data_str1, '%d/%m/%Y')
data2 = datetime.strptime(data_str2, '%d/%m/%Y')

# Calcule a diferença entre as datas
diferenca = abs((data2 - data1).days)

# Exiba a diferença em dias
print(f"A diferença entre as datas é de {diferenca} dias.")
