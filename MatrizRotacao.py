import numpy as np

theta = np.radians(30)

sen = np.sin(theta)
cos = np.cos(theta)

mr = np.array(((cos, -sen), (sen, cos)))
              
print('Matriz de rotação:')
print(mr)

vetor = np.array((0,1)) #O VETOR COLUNA É CORRESPONDENTE A MATRIZ [X1 Y1]

print('Vetor v: ')
print(vetor)

# O VETOR ROTACIONADO [X2 Y2] É DEFINIDO POR MEIO DO PRODUTO ESCALAR ENTRE MR * VETOR E DENOMINADO VETOR'

vr = mr.dot(vetor) # O COMANDO .DOT É USADO PARA O CÁLCULO DO PRODUTO ESCALAR 

print('O Vetor rotacionado é igual a: ')
print(vr)
