def inversor(phrase):
  return ' '.join(phrase.split()[::-1])

def dmas(s):
  debug = s[2:7:3]
  if s[2:7:3] == '--':
    return s.split('-')
  elif s[2:7:3] == '//':
    return s.split('/')
  else:
    return s
  
def anagrama(s1, s2):
  return sorted(s1) == sorted(s2)
  
  
#Ex1 Testes
print(inversor('batatinha quando nasce'))
print()

#Ex2 Testes  
print(dmas('15/12/2024'))
print(dmas('15-12-2024'))
print(dmas('15/12-2024'))
print(dmas('15 de dezembro de 2024'))
print(dmas(''))

#Ex3 Testes
print(anagrama('alegria', 'alergia'))
print(anagrama('bacana','banana'))
print(anagrama('voo','ovo'))
print(anagrama('nora','orna'))