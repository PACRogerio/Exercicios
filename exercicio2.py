print ("Exercício 2")
print ('')
print ("Construa um array unidimensional com 30 números inteiros")
print ("escolhidos de forma randômica no intervalo entre 0 e 20.")
print ("Reformate o array para que se torne uma matriz `A` com 5 linhas e 6 colunas.")
print('')
# Importa a biblioteca NumPy e atribui o apelido 'np' para facilitar o uso das funções
import numpy as np

# Gera um array 1D com 30 números inteiros aleatórios no intervalo de 0 a 20 (incluindo o 20)
# Sintaxe: np.random.randint(início, fim_exclusivo, quantidade)
# Nota: Usamos 21 para que o número 20 também possa ser sorteado
array_1d = np.random.randint(0, 21, size=30)

# Redimensiona (reformata) o array de 30 elementos para uma matriz de 5 linhas e 6 colunas
# O número total de elementos deve se manter o mesmo (5 * 6 = 30)
A = array_1d.reshape(5, 6)

# Exibe o array unidimensional original criado
print("Array unidimensional original (observe que o exercicio omite a informação de não repetição de numeros):")
print(array_1d)

# Exibe a matriz A formatada (5x6)
print("\nMatriz A (5 linhas x 6 colunas):")
print(A)