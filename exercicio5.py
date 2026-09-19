print ("Exercício 5\n")
print ("Construa um array `A` com 20 linhas e 10 colunas")
print ("onde os elementos são os números interios de  1 até 200.\n")
print ("- Crie uma __view__ de `A` chamada `A_lpares` contendo apenas as linhas de `A` com índice par.")
print ("- Crie uma __view__ de `A` chamada `A_lpares_cimpares` contendo as linhas `A` com índice par")
print ("  e colunas com índice ímpar.\n")
# Importa a biblioteca NumPy e dá a ela o apelido de np
import numpy as np

# Cria números de 1 até 200
# O 201 não entra, por isso usamos 201
# Depois organiza os 200 números em 20 linhas e 10 colunas
A = np.arange(1, 201).reshape(20, 10)

# Cria uma VIEW de A
# ::2 nas linhas significa:
# começar no índice 0 e andar de 2 em 2
# Portanto, seleciona as linhas de índice par:
# 0, 2, 4, 6, ..., 18
#
# O ":" nas colunas significa:
# selecionar todas as colunas
A_lpares = A[::2, :]

# Cria outra VIEW de A
# ::2 nas linhas -> linhas de índice par
# 1::2 nas colunas -> começar no índice 1
# e andar de 2 em 2:
# 1, 3, 5, 7, 9
#
# Portanto:
# linhas pares + colunas ímpares
A_lpares_cimpares = A[::2, 1::2]

# Mostra o array original
print("A:")
print(A)

# Mostra as linhas de índice par
print("\nA_lpares:")
print(A_lpares)

# Mostra as linhas pares e colunas ímpares
print("\nA_lpares_cimpares:")
print(A_lpares_cimpares)
