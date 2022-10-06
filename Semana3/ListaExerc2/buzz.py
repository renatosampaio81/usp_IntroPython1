# Exercício 03
# Receba um número inteiro na entrada e imprima "Buzz" se o número for divisível por 5.
# Caso contrário, imprima o mesmo número que foi dado na entrada.

numero = 0
resto = 0.00

numero = input("Entre com o um número inteiro: ")

resto = int(numero)%5
if resto == 0 :
  print('Buzz')
else :
  print(numero)