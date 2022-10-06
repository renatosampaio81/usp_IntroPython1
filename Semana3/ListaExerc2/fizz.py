# Exercício 2
# Receba um número inteiro na entrada e imprima "Fizz" se o número for divisível por 3.
# Caso contrário, imprima o mesmo número que foi dado na entrada.

numero = 0
resto = 0.00

numero = input("Entre com o um número inteiro: ")

resto = int(numero)%3
if resto == 0 :
  print('Fizz')
else :
  print(numero)