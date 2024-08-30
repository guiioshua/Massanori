import random
'''
#Ex1
numeros = random.sample(range(1,101), 10)
numeros.sort()
print(f'Da lista de números {numeros}, o menor é {numeros[0]} e o maior é {numeros[-1]}.')
'''
'''
#Ex2
numeros = random.sample(range(1,101), 20)
pares, ímpares =[], []

for numero in numeros:
    if numero % 2 ==0:
        pares.append(numero)
    else:
        ímpares.append(numero)
print(f'LISTA: {numeros}\nPARES: {pares}\nÍMPARES: {ímpares}')
'''

'''
#Ex3
numeros1 = random.sample(range(1,101), 10)
numeros2 = random.sample(range(1,101), 10)
numeros3 = []
for i in range(0,len(numeros1),2):
    numeros3.append(numeros1[i])
    numeros3.append(numeros2[i+1])
for i in range(0,len(numeros1),2):
    numeros3.append(numeros2[i])
    numeros3.append(numeros1[i+1])
print(f"{numeros1}\n{numeros2}\n{numeros3}")
'''

#Ex4
statement = 'The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.'
statement = statement.split()
for letra in statement:
    
