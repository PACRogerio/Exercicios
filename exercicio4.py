print ("Exercício 4\n")
print ("Construa um array `A` bidimensional 5x6 com 30 números inteiros escolhidos de forma randômica")
print ("no intervalo entre 0 e 20.\n") 
print ("- faça uma cópia do array `A` criado, chamando a cópia de `Ac`")
print ("- Substitua todos os elementos do array `A` que sejam maiores que 10 pelo valor -1") 
print ("- Substitua todos os elementos do array `Ac` que sejam maiores que 7 e menores que 15 pelo valor -1\n") 

print ("__Dica:__ Gere máscaras booleanas para realizar as modificações nos arrays.\n")
import numpy as np

# 1. Criação do array A (5x6 com inteiros randômicos entre 0 e 20)
np.random.seed(42)  # Opcional: fixa a semente para gerar sempre os mesmos números
A = np.random.randint(0, 21, size=(5, 6))

print("--- Array A Original ---")
print(A,"\n")

# 2. Cópia do array A chamando-se Ac
Ac = A.copy()
print("--- Array Ac ---")
print(Ac)

# 3. Substituição no array A: elementos maiores que 10 por -1
mascara_A = A > 10
A[mascara_A] = -1

print("\n--- Array A (elementos > 10 substituídos por -1) ---")
print(A)

# 4. Substituição no array Ac: elementos > 7 E < 15 por -1
mascara_Ac = (Ac > 7) & (Ac < 15)
Ac[mascara_Ac] = -1

print("\n--- Array Ac (elementos entre 8 e 14 substituídos por -1) ---")
print(Ac)