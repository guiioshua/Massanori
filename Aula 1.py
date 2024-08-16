#a = int(input("Primeiro valor: "))
#b = int(input("Segundo valor: "))
#if a > b:
#    print ("O primeiro número é maior!")
#if b > a:
#    print ("O segundo número é maior!")
#else:
#    print("Os dois números são iguais!")

#idade = int(input("Digite a idade de seu carro"))
#if idade <= 3:
#    print("Novo")
#else:
#    print("Velho")

#velocidade = int(input("Qual a velocidade do carro?"))
#if velocidade > 110:
#    multa = (velocidade - 110) * 5
#    print(f'Multa! A multa é de R$ {multa:.2f}!')

minutos = int(input("Minutos: "))
if minutos < 200:
    conta = float (0.2 * minutos) 
if 200 <= minutos <= 400:
    conta = float (0.18 * minutos)
if minutos > 400:
    conta = float (0.15 * minutos)

print(f"A conta é de R${conta:.2f}.")
