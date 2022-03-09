# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 15:48:42 2022

@author: Vitor
"""

import math

x0 = int(input('Informe o valor de X0:'))
x1 = int(input('Informe o valor de X1:'))

y0 = int(input('Informe o valor de Y0:'))
y1 = int(input('Informe o valor de Y1:'))


L2 = int(input('Informe o valor de L2:'))
L3 = int(input('Informe o valor de L3:'))

L = math.sqrt((x1-x0)**2 + (y1-y0)**2)

alpha = math.atan((y1-y0)/(x1-x0))
theta1 = math.atan((y1-y0)/(x1-x0)) +- (math.acos((L2**2 + L**2 - L3**2))
theta2 = math.acos((L2**2 + L**2 - (L3**2)))
phi = math.acos((L2**2 + L**2 - L3**2))
beta = 180 - theta2

print('"""""""""""""""""""""""""""""""""""')
print('Valor de L: ',L)
print('Valor de Alpha: ',alpha)
print('Valor de Theta1: ',theta1)
print('Valor de Theta2: ',theta2)
print('Valor de Phi: ',phi)
print('Valor de Beta: ',beta)
print('"""""""""""""""""""""""""""""""""""')