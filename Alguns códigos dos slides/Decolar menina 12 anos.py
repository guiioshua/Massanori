def esconde(frase):
    resp = ''
    for c in frase:
        resp = resp + chr(ord(c) + 40000)
    return resp

def mostra(frase):
    resp = ''
    for c in frase:
        resp = resp + chr(ord(c) - 40000)
    return resp

