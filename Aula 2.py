'''
fim = int(input('Fim: '))
x = 0
while x <= fim:
    print(x)
    x = x + 2 #acumulador
'''

'''
soma = 0
x = 1 #contador simples
while x <= 3:
    n = int(input('Numero: '))
    soma = soma + n #acumulador
    x = x + 1
prit(soma)
'''

'''
x = 1
soma = 0
while x <= 10:
    n = int(input('Digite o número: '))
    soma = soma + n
    x = x + 1
print (soma/10)
'''

'''
fatorial = int(input('Fatorial de: '))
contador = 1
acumulador = 1
while contador <= fatorial:
    acumulador = acumulador * contador
    contador = contador + 1
print(acumulador)
'''

soma = 0
while True:
    x = int(input('n (zero sai): ' ))
    if x == 0:
        break
    soma = soma + x
print(f'Soma: {soma}')