'''#Ex1
a = float(input('Lado a:'))
b = float(input('Lado b:'))
c = float(input('Lado c:'))
if a+b>c and a+c>b and c+b>a:
    print('Pode ser um triângulo')
    if a==b==c:
        print('É um triângulo equilátero')
    elif a==b or a==c or b==c:
        print('É um triângulo isóceles')
    else:
        print ("É um triângulo escaleno")

else: print('Não pode ser um triângulo')
'''

'''#Ex2
ano = int(input('Digite o ano: '))
if ano % 4 == 0:
    if ano % 400 == 0:
        print('O ano é bissexto')
    elif ano % 100 == 0:
        print('O ano não é bissexto')
    else: print('O ano é bissexto')

else: print('O ano não é bissexto')
'''

'''#Ex3
peso = float(input('Digite o peso dos peixes: '))
exceco = (peso - 50)
multa = exceco * 4
if peso > 50:
    print(f'EXCEÇO: {exceco}KG\nMULTA: R${multa:.2f}')
else: 
    exceco = 0
    multa  = 0
    print(f'EXCEÇO: {exceco}KG\nMULTA: R${multa:.2f}')
'''

#Ex4
'''
a = int(input('Digíte o primeiro número:'))
b = int(input('Digíte o segundo número:'))
c = int(input('Digíte o terceiro número:'))

if a > b and a > c:
    print('O primeiro é o maior número')
if b > a and b > c:
    print('O segundo é o maior número')
if c > a and c > b:
    print('O terceiro é o maior número')         
'''

#Ex5 fazer uma função com um uma variavel 'maior' = ao primeiro elemento de abc e um loop for numero in abc que substitui o maior com o elemento do array caso ele for > q o maior
a = int(input('Digíte o primeiro número:'))
b = int(input('Digíte o segundo número:'))
c = int(input('Digíte o terceiro número:'))

abc = [a, b, c]
def maior = (abc)


