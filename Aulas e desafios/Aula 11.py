#Ex1
def calculaGraos():
  grao = 0
  grao1 = 1
  for n in range(64):
    grao += grao1
    grao = grao*2
  return grao

print(calculaGraos())

#Ex2
def pi(n):
  numerador = 4
  denominador = 1
  pi = numerador/denominador
  for iteração in range (n):
    denominador += 2
    if iteração % 2 == 0:
      pi -= (numerador/denominador)
    else:
      pi += (numerador/denominador)

  return pi
  
print(pi(10000))