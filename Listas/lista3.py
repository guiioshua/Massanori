#Ex1
x = int(input('NOTA: '))
while x<0 or x>10:
    x = int((input('VALOR INVÁLIDO, DIGITE NOVAMENTE: ')))
else: print(f'NOTA: {x}')


#Ex2
while input('USUÁRIO: ') == input('SENHA: '):
    print('ERRO: O USUÁRIO E A SENHA NÃO PODEM SER IGUAIS')
else: print('VOCÊ É FELIZ')


#Ex3
x = 0
while 80000*(1.03)**x<200000*(1.015)**x:
    x = x + 1
print(f'Vai levar {x} anos para que a população de A iguale a de B.')



#Ex4
n1, n2 = 1, 1
for i in range (int(input('Fn: '))-1):
    n1, n2 = n2, n1+n2
print(n1)



#Ex5
n1 = int(input('PRIMEIRO NÚMERO: '))
n2 = int(input('SEGUNDO NÚMERO: '))

while n1 % n2 != 0:
    n1, n2 = n2, n1 % n2
    
print(f'O MDC É: {n2}')
