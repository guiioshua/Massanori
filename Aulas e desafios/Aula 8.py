def binario(n, k):
    resposta = []
    for i in range(2**n):
        resposta.append(bin(i))
    return resposta

def acha1(numero):
    return numero.count('1')

k = int(input('k: '))
n = int(input('n: '))
print(sorted(binario(n,k), key = acha1, reverse = True)[k-1])
