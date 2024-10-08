# Coding Dojo


# fizzbuzz
# Seja um inteiro positivo n, devolve 'Fizz' se ele for
# divisível por 3, 'Buzz' se for divisível por 5,
# 'FizzBuzz' se (for divisível ao mesmo tempo por 3 e 5
# e o inteiro n em todos os outros casos
def fizzbuzz(n):
  return 'FizzBuzz' if n%5==0 and n%3==0 else('Fizz' if n%3==0 else ('Buzz' if n%5==0 else n))


# soma múltiplos de 3 ou 5
# soma todos os múltiplos de 3 ou 5 abaixo de um inteiro n
# soma(5) -> 3    soma(10) -> 23 = 3 + 5 + 6 + 9
# soma(20) -> 78 = 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18
def soma(n):
  i = 0
  for k in range(n):
    if k%3==0 or k%5==0:
      i += k    
  return i


# vogais_consecutivas
# Seja um texto, com maíusculas e minúsculas. Retorne a maior
# sequência de vogais. vogais_consecutivas('abacate') -> 1
# vogais_consecutivas('beautiful') -> 3
# vogais_consecutivas('xaaxeeexiixooooxuu') -> 4
# vogais_consecutivas('AaEeIiOoUu') -> 10
def vogais_consecutivas(texto):
    resultado = []
    i=0
    k=0
    while k < len(texto):
        if texto[k] in 'aeiouAEIOU':
            i+=1
            k+=1
        else: 
            resultado.append(i)
            i=0
            k+=1
    else: resultado.append(i)
    return max(resultado)



# papagaio
# temos um papagaio que fala alto
# hora é um parâmetro entre 0 e 23
# temos problemas se o papagaio estiver falando
# antes da 7 ou depois das 20
def papagaio(falando, hora):
  return falando if hora<7 or hora>20 else not falando


# apaga
# seja uma string s e um inteiro n
# retorna uma nova string sem a posição n
# apaga('kitten', 1) -> 'ktten'
# apaga('kitten', 4) -> 'kittn'
def apaga(s, n):
  return s[:n]+s[n+1:]


# troca
# seja uma string s
# se s tiver tamanho <= 1 retorna ela mesma
# caso contrário troca a primeira e última letra
# troca('code') -> 'eodc'
# troca('a') -> 'a'
# troca('ab') -> 'ba'
def troca(s):
  return s if len(s)<=1 else s[-1:]+s[1:-1]+s[0]


# string_splosion
# string_splosion('Code') -> 'CCoCodCode'
# string_splosion('abc') -> 'aababc'
# string_splosion('ab') -> 'aab'
def string_splosion(s):
  resultado = ''
  for k in range(len(s)):
    resultado+=s[:k+1]
  return resultado


# roda2
# rodar uma string s duas posições
# a string possui pelo menos 2 caracteres
# left2('Hello') -> 'lloHe' elloH lloHe
# left2('Hi') -> 'Hi'
def roda2(s):
  return s[2:]+s[:2]


# sum2 #
# Dada uma lista de inteiros de qualquer tamanho
# retorna a soma dos dois primeiros elementos
# se a lista tiver menos de dois elementos, soma o que for possível
def sum2(nums):
    return sum(nums[:2]) if len(nums) >=2 else (nums[0] if len(nums) == 1 else 0)


# G. date_fashion
# você e sua namorada(o) vão a um restaurante
# eu e par são as notas das suas roupas de 0 a 10
# quanto maior a nota mais chique vocês estão vestidos
# o resultado é se vocês conseguiram uma mesa no restaurante:
# 0=não 1=talvez e 2=sim
# se a nota da roupa de um dos dois for menor ou igual a 2
# vocês não terão direito à uma mesa (0)
# se as notas são maiores, então caso um dos dois esteja
# bem chique (nota >= 8) então a resposta é sim (2)
# caso contrário a resposta é talvez (1)
# date_fashion(5, 10) -> 2
# date_fashion(5, 2) -> 0
# date_fashion(5, 5) -> 1
def date_fashion(eu, par):
  if eu <= 2 or par <= 2:
    return 0
  elif eu >= 8 or par >=8:
    return 2
  else: return 1


# H. squirrel_play
# os esquilos na FATEC brincam quando a temperatura está entre 60 e 90
# graus Fahreneit (são estrangeiros e o termômetro é diferente rs)
# caso seja verão, então a temperatura superior é 100 no lugar de 90
# retorne True caso os esquilos brinquem
# squirrel_play(70, False) -> True
# squirrel_play(95, False) -> False
# squirrel_play(95, True) -> True
def squirrel_play(temp, is_summer):
  return temp >= 60 and temp <= 100 if is_summer else temp >= 60 and temp <= 90


# I. pego_correndo
# você foi pego correndo
# o resultado será:
# sem multa = 0
# multa média = 1
# multa grave = 2
# velocidade <= 60 sem multa
# velocidade entre 61 e 80 multa média
# velocidade maior que 81 multa grave (cidade do interior)
# caso seja seu aniversário a velocidade pode ser 5 km/h maior em todos os casos
# pego_correndo(60, False) -> 0
# pego_correndo(65, False) -> 1
# pego_correndo(65, True) -> 0 
def pego_correndo(speed, is_birthday):
  if is_birthday:
    return 0 if speed <= 65 else(2 if speed >= 86 else 1)
  return 0 if speed <= 60 else(2 if speed >= 81 else 1)


# J. alarm_clock #
# day: 0=domingo, 1=segunda, 2=terça, ..., 6=sábado
# vacation = True caso você esteja de férias
# o retorno é uma string que diz quando o despertador tocará
# dias da semana '07:00'
# finais de semana '10:00'
# a menos que você esteja de férias, neste caso:
# dias da semana '10:00'
# finais de semana 'off'
# alarm_clock(1, False) -> '7:00'
# alarm_clock(5, False) -> '7:00'
# alarm_clock(0, False) -> '10:00'
def alarm_clock(day, vacation):
  if vacation:
    return '10:00' if 0<day<6 else 'off'
  else: return '7:00' if 0<day<6 else '10:00'


# Provided simple test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Parabéns!'
  else:
    prefixo = ' Ainda não'
  print ('%s obtido: %s esperado: %s'
         % (prefixo, repr(obtido), repr(esperado)))


def main():
  print ('fizzbuzz')
  test(fizzbuzz(1), 1)
  test(fizzbuzz(2), 2)
  test(fizzbuzz(3), 'Fizz')
  test(fizzbuzz(4), 4)
  test(fizzbuzz(5), 'Buzz')
  test(fizzbuzz(6), 'Fizz')
  test(fizzbuzz(7), 7)
  test(fizzbuzz(15), 'FizzBuzz')
  test(fizzbuzz(30), 'FizzBuzz')
  print ()
  
  print ('soma')
  test(soma(1), 0)
  test(soma(5), 3)
  test(soma(10), 23)
  test(soma(20), 78)
  print ()
  
  print ('vogais_consecutivas')
  test(vogais_consecutivas('xxxx'), 0)
  test(vogais_consecutivas('abacate'), 1)
  test(vogais_consecutivas('beautiful'), 3)
  test(vogais_consecutivas('xaaxeeexiixooooxuu'), 4)
  test(vogais_consecutivas('AaEeIiOoUu'), 10)


  print ()
  print ('Papagaio')
  test(papagaio(True, 6), True)
  test(papagaio(True, 7), False)
  test(papagaio(False, 6), False)
  test(papagaio(True, 21), True)
  test(papagaio(False, 21), False)
  test(papagaio(True, 23), True)
  test(papagaio(True, 20), False)


  print ()
  print ('Apaga')
  test(apaga('kitten', 1), 'ktten')
  test(apaga('aaaaaa', 3), 'aaaaa')
  test(apaga('kitten', 0), 'itten') 
  test(apaga('kitten', 4), 'kittn')
  test(apaga('Hi', 0), 'i')
  test(apaga('Hi', 1), 'H')
  test(apaga('code', 0), 'ode')
  test(apaga('code', 1), 'cde')
  test(apaga('code', 2), 'coe')
  test(apaga('code', 3), 'cod')
  test(apaga('chocolate', 8), 'chocolat')


  print ()
  print ('Troca letras')
  test(troca('code'), 'eodc')	    
  test(troca('a'), 'a')
  test(troca('ab'), 'ba')
  test(troca('abc'), 'cba')
  test(troca(''), '')
  test(troca('Chocolate'), 'ehocolatC')
  test(troca('nythoP'), 'Python')
  test(troca('hello'), 'oellh')
  
  print ()
  print ('String Explosion')
  test(string_splosion('Code'), 'CCoCodCode')
  test(string_splosion('abc'), 'aababc')
  test(string_splosion('ab'), 'aab')
  test(string_splosion('x'), 'x')
  test(string_splosion('fade'), 'ffafadfade')
  test(string_splosion('There'), 'TThTheTherThere')
  test(string_splosion('Kitten'), 'KKiKitKittKitteKitten')
  test(string_splosion('Bye'), 'BByBye')
  test(string_splosion('Good'), 'GGoGooGood')
  test(string_splosion('Bad'), 'BBaBad')


  print ()
  print ('Roda 2')
  test(roda2('Hello'), 'lloHe')
  test(roda2('python'), 'thonpy')
  test(roda2('Hi'), 'Hi')
  test(roda2('code'), 'deco')
  test(roda2('cat'), 'tca')
  test(roda2('12345'), '34512')
  test(roda2('Chocolate'), 'ocolateCh')
  test(roda2('bricks'), 'icksbr')


  print ()
  print ('sum2')
  test(sum2([1, 2, 3]), 3)
  test(sum2([1, 1]), 2)
  test(sum2([1, 1, 1, 1]), 2)
  test(sum2([1, 2]), 3)
  test(sum2([1]), 1)
  test(sum2([]), 0)
  test(sum2([4, 5, 6]), 9)
  test(sum2([4]), 4)


  print ()
  print ('date fashion')
  test(date_fashion(5, 10), 2)
  test(date_fashion(5, 2), 0)
  test(date_fashion(5, 5), 1)
  test(date_fashion(3, 3), 1)
  test(date_fashion(10, 2), 0)
  test(date_fashion(2, 9), 0)
  test(date_fashion(9, 9), 2)
  test(date_fashion(10, 5), 2)
  test(date_fashion(2, 2), 0)
  test(date_fashion(3, 7), 1)
  test(date_fashion(2, 7), 0)
  test(date_fashion(6, 2), 0)


  print ()
  print ('squirrel_play')
  test(squirrel_play(70, False), True)
  test(squirrel_play(95, False), False)
  test(squirrel_play(95, True), True)
  test(squirrel_play(90, False), True)
  test(squirrel_play(90, True), True)
  test(squirrel_play(50, False), False)
  test(squirrel_play(50, True), False)
  test(squirrel_play(100, False), False)
  test(squirrel_play(100, True), True)
  test(squirrel_play(105, True), False)
  test(squirrel_play(59, False), False)	
  test(squirrel_play(59, True), False)	
  test(squirrel_play(60, False), True)


  print ()
  print ('Pego correndo')
  test(pego_correndo(60, False), 0)
  test(pego_correndo(65, False), 1)
  test(pego_correndo(65, True), 0)
  test(pego_correndo(80, False), 1)
  test(pego_correndo(85, False), 2)
  test(pego_correndo(85, True), 1)
  test(pego_correndo(70, False), 1)
  test(pego_correndo(75, False), 1)
  test(pego_correndo(75, True), 1)
  test(pego_correndo(40, False), 0)
  test(pego_correndo(40, True), 0)
  test(pego_correndo(90, False), 2)


  print ()
  print ('Alarm Clock')
  test(alarm_clock(1, False), '7:00')
  test(alarm_clock(5, False), '7:00')
  test(alarm_clock(0, False), '10:00')
  test(alarm_clock(6, False), '10:00')
  test(alarm_clock(0, True), 'off')
  test(alarm_clock(6, True), 'off')
  test(alarm_clock(1, True), '10:00')
  test(alarm_clock(3, True), '10:00')
  test(alarm_clock(5, True), '10:00')




if __name__ == '__main__':
  main()