'''
def efeito_avalanche(string):
    novaString = ''
    for k in range(len(string)):
        novaString += string[:k]
    return print(novaString+string)
efeito_avalanche(input("Digite a string: "))
'''

'''
def club_vip (nota1, nota2):
    if nota1 <= 2 or nota2 <= 2:
        return 0
    if nota1 >= 8 or nota2 >= 8:
        return 2
    return 1

print(club_vip(5, 5))
'''

def aventura_x(lista):
    listaComX = []
    listaSemX = []
    for palavra in lista:
        for letra in palavra:
            if letra == 'x':
                listaComX.append(palavra)
                
        