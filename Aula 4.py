'''
palavra = abacate
k=0

while k<len(palavra)
    print(palavra[k])
    k=k+1
#equivale a
for x in palavra: print (x)
'''

'''
lista = 'batatinha quando nasce'
lista.split()
k=0
while k < len(lista):
    p = lista[k]
    print(p)
    k = k+1
#equivale a
for palavra in lista: print (palavra)
'''

'''
for x in range(4):
    print(x)
    #range vai de um intervalo de 0 até antes de 4 (3)
for x in range(1,7):
    print(x)
    #range vai de um intervalo de 1 até antes de 7 (6)
for x in range(1,7,2):
    print(x)
    #mesmo de antes, mas ele incrementa de 2 em 2
'''

import random
#print(dir(random))
#help(random.randint)
'''
print(random.randint(1, 100)) #um numero aleatório entre 1 e 100
print(random.sample(range(1,101),10)) #um array de 10 elementos com numeros aleatórios da amostra da range de
                                      # 1 a 101 (100)
'''

'''
nomes = 'ana emanuele julia  lavinia maria tatiane'
nomes = nomes.split( )
print(nomes)

random.shuffle(nomes)
print(nomes)

nomes.sort(reverse=True) #organiza em ordem alfabética ao contrario
print(nomes)

nomes.sort(key=len) #organiza de acordo com o número de letras crescente
'''

'''
def é_par(n):
    if n%2 == 0:
        return True
    else:
        return False
print(é_par())
'''
#ex 3 lista IV
lista = random.sample(range(1,101), 10)
lista2 = random.sample(range(1,101), 10)

#ex 4 list IV
frase = '''The Python Software Foundation and the global Python
community welcome and encou
rage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your backgrou
nd, we welcome you.'''
frase = frase.replace(',', ' ')
frase = frase.replace('.',' ')
frase = frase.replace(':', ' ')
frase = frase.lower()
frase = frase.split()

#ex 5 fazer uma função pra calcular numero de palavras

#lista V
n = random.randint(1,999999)
print (n)
