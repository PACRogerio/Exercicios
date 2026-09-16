print ("Exercício 3")
print('')
print ("Crie uma __view__ da matriz `A` gerada na célula anterior contendo:")
print ("- as linhas de `A` com índices 0,1 e 3")
print ("- as linhas de `A` com índice 1 e 2 e as colunas com índice 0,2 e 4")
print ("- as linhas de `A` com índice 1 e 3 e as colunas com índice 1 e 3")
print('')
import numpy as np

# Reconstrução da Matriz A (5x6) para o exercício
array_1d = np.random.randint(0, 21, size=30)
A = array_1d.reshape(5, 6)

# Exibe a matriz original no terminal
print("================ MATRIZ A ORIGINAL ================")
print(A)
print('')


# --- ITEM 1 ---
# A[[0, 1, 3], :] significa:
# - [0, 1, 3] -> Seleciona especificamente as linhas de índice 0, 1 e 3.
# - ,         -> Separa a seleção de linhas da seleção de colunas.
# - :         -> O símbolo de dois-pontos isolado indica "todas as colunas".
view_1 = A[[0, 1, 3], :]

print("Item 1) As linhas de A com índices 0, 1 e 3:")
print(view_1)
print("-" * 50)


# --- ITEM 2 ---
# np.ix_([1, 2], [0, 2, 4]) significa:
# - np.ix_    -> Função que cruza os índices para formar uma submatriz/grade perfeita.
# - [1, 2]    -> Seleciona as linhas de índice 1 e 2.
# - [0, 2, 4] -> Seleciona as colunas de índice 0, 2 e 4.
view_2 = A[np.ix_([1, 2], [0, 2, 4])]

print("Item 2) As linhas de A com índice 1 e 2 e as colunas com índice 0, 2 e 4:")
print(view_2)
print("-" * 50)


# --- ITEM 3 ---
# np.ix_([1, 3], [1, 3]) significa:
# - np.ix_ -> Realiza o cruzamento das linhas e colunas especificadas.
# - [1, 3] -> Seleciona as linhas de índice 1 e 3 (primeiro argumento).
# - [1, 3] -> Seleciona as colunas de índice 1 e 3 (segundo argumento).
view_3 = A[np.ix_([1, 3], [1, 3])]

print("Item 3) As linhas de A com índice 1 e 3 e as colunas com índice 1 e 3:")
print(view_3)
print("-" * 50)
