#EXERCÍCIOS PYTHON ROBÓTICA

#EXERCÍCIO 1 

L = [5,7,2,9,4,1,3]

print('O tamanho da lista é igual a:', len(L), 'números')
print('O maior valor da lista é o número', max(L))
print('O menor valor da lista é o número', min(L))
print('A soma dos valores da lista é igual a:',sum(L))
print('A lista em ordem crescente fica:', sorted(L))
print('A lista em ordem crescente fica:', sorted(L, reverse = True))

#EXERCÍCIO 2

import math

X = int(input('Informe o Valor de X:'))
Y = int(input('Informe o Valor de Y:'))

Z = (math.pow(X, 2) + math.pow(Y, 2)) * ((X - Y) ** 2)
print(Z)

#EXERCÍCIO 3

D = {"Salgado" : 4.50, 
     "Lanche" : 6.50, 
     "Suco" : 3.00, 
     "Refrigerante" : 3.50, 
     "Doce" : 1.00}

print(D)
print(D.values())
print(D.keys())

#EXERCÍCIO 4

import statistics
N = {"João" : 7.50, "Gabriela" : 8.0, "Felipe" : 5.60, "André" : 6.90, "Mariana" : 7.8}
Media = statistics.mean(N.values())
print("A média entre as notas dos 5 alunos é igual a:", Media)

#EXERCÍCIO 5 

#RESOLUÇÃO USANDO FUNÇÃO

N1 = float(input("Digite a primeira nota: "))
N2 = float(input("Digite a segunda nota:  "))

def media(N1,N2):
    M = (N1 + N2) / 2
    if M >= 6.0:
            print("O aluno ficou com a média:",M,"e está aprovado.")
    else:
            print("O aluno ficou com a média:",M,"e está reprovado.")
media(N1,N2)

#RESOLUÇÃO USANDO IF

if M >= 6.0:
        print("O aluno ficou com a média:",M,"e está aprovado.")
else:
        print("O aluno ficou com a média:",M,"e está reprovado.")
   
#EXERCÍCIO 6

N1 = float(input("Digite a primeira nota: "))
N2 = float(input("Digite a segunda nota:  "))

def media(N1,N2):
    M = (N1 + N2) / 2
    if M >= 6.0:
            print("O aluno ficou com a média:",M,"e está aprovado.")
    elif M >= 4:
            print("O aluno ficou com a média:",M,"e está de exame.")
    else:
            print("O aluno ficou com a média:",M,"e está de reprovado.")
media(N1,N2)

#EXERCÍCIO 7

s = 0

for x in range(3,334,3):
   s = s + x
print("Soma = ",s)
    
#EXERCÍCIO 8

i = 0

for leitura in range(1,11):
    nota = float(input("Informe a nota " +str(leitura)+":"))
    i = i + nota
    m = i/10
print(f'Média: {m:.2f}')

#EXERCÍCIO 9

num = int(input("Digite um número para determinar a sua tabuada:"))

for i in range(1,11):
    print('{} x {} = {}'.format(num, i, num*i))
    
    
