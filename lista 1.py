#Ex1
print("A soma dos dois números é:", int(input("Digite o primeiro número: "))+int(input("Digite o segundo número: ")))

#Ex2
converter = int(input("Digíte o valor em metros: "))
print (f"O valor de {converter} metros em milímetros é:", converter * 1000, "milímetros.")

#Ex3
print ('O total em segundos é: ', (int(input("Dia: "))*60*60*24 + int(input("Horas: "))*60*60 + int(input("Minutos: "))*60 + int(input("segundos: "))))

#Ex4
salario = float(input("Digite o seu salario: "))
acrescimo = float(input("Digite o valor da porcentagem de acrescimo: "))
print (f"O acrescimo è de R${(salario * (1 + acrescimo / 100)) - salario}\nO novo valor do salário será de R${salario*(1+acrescimo/100)}")

#Ex5
price = float(input("Digite o preço da mercadoria em reais: "))
discount = float(1 - float(input("Digite o desconto em procentagem: ")) / 100)
print (f'O desconto é de R${(price - price*discount):.2f}\nO preço com desconto é de R${(price*discount):.2f}')

#Ex6
print('O tempo da viagem é de', float(input('Qual a distância percorrida, em km? ')) / float(input('Qual a velocidade do carro, em km/h? ')), 'horas.' )

#Ex7
print('A temperatura em Fahrenheit é de ', float(input('Digite a temperatura em graus Celsius: ')) * 9 / 5 + 32 )

#Ex8
print(f'A temperatura em Celsius é de ', (float(input('Digite a temperatura em graus Farenheit: ')) -32) * 5 / 9)

#Ex9
print('O preço a pagar é: R$', float(input('Quantos km voce percorreu? ')) * 0.15 + float(input('Por quantos dias o carro foi alugado? ')) * 60)

#Ex10
print(f'Voce perdeu ', int(int(input('Quantos cigarros voce fuma por dia? ')) / 144  *  int(input('Você fuma há quantos anos? ')) *365), 'dias de vida.')

#Ex11
import sys
sys.set_int_max_str_digits(350000)
print('2 elevado a 1.000.000 possui ', len(str(2**1000000)), 'números.')