'''
predio = ['zelador', 'Família Silva', 'Romeu', 'Dona Julieta']
predio.append('Dona Pafuncia')
x=0
while x <len(predio):
    print(predio[x])
    x=x+1
'''

'''
notas = []
x = 0
while x < 5:
    notas.append(float(input(f'NOTA {x+1}: ')))
    x = x + 1
x = 0
soma = 0
while x < len(notas):
    soma = soma + notas[x]
    x = x + 1
media = soma/len(notas)
print(media)
'''

'''
lista = ['batatinha', 'quando','nasce','esparrama','pelo','chão']
x = 0
while x < len(lista):
    if len(lista[x]) > 7:
        print(lista[x])
    x = x+1
'''

'''#data=input('Digite a data em formato dd/mm/aaaa')
meses, meses2,meses3, meses4,meses5, meses6,meses7, meses8,meses9, meses10,meses11, meses12 = ('janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro').split()
print(meses4)
'''

texto = 'batatinha quando nasce'
lista = texto.split()
lista2 = ' '.join(lista)
print(lista2)

print(dir(texto))
help(str)
