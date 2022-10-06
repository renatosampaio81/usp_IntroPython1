# Exercício 4
# Receba um número inteiro na entrada e imprima "FizzBuzz" se o número for divisível por 3 ou 5.
# Caso contrário, imprima o mesmo número que foi dado na entrada.

numero = 0
resto3 = 0.00
resto5 = 0.00

numero = input("Entre com o um número inteiro: ")

resto3 = int(numero)%3
resto5 = int(numero)%5

if (resto3 == 0) or (resto5 == 0):
  print('FizzBuzz')
else :
  print(numero)