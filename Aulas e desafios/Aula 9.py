def somaString (s):
    resposta = ''
    for n in range(len(s)+1):
        resposta += s[:n]
    return print(resposta)
somaString('Code')

def hífenizador(frase):
    fraseSplitada = frase.split()
    return print('-'.join(fraseSplitada))
hífenizador('batatinha quando nasce')

