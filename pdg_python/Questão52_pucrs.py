import math

# Solicite ao usuário que digite o valor de N e p
n = int(input("Digite o valor de N: "))
p = int(input("Digite o valor de p: "))

# Verifique se p é menor ou igual a N
if p <= n:
    combinacao = math.comb(n, p)
    arranjo = math.perm(n, p)
    
    print(f"Combinação de {n} elementos em {p} subconjuntos: C({n}, {p}) = {combinacao}")
    print(f"Arranjo de {n} elementos em {p} subconjuntos: A({n}, {p}) = {arranjo}")
else:
    print("O valor de p deve ser menor ou igual a N.")
