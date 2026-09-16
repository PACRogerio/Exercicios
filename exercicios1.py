# Exercício 1)
# Utilize comprehension para gerar a lista de todos os números interios entre 0 e 19. 
# Converta a lista em um array bidimensional (matriz) com 4 linhas
#  e 5 colunas.
#
import numpy as np

numeros = [x for x in range(20)]
matriz = np.array(numeros).reshape(4, 5)

print(matriz)