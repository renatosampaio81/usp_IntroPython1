# Exercício 1 - Par ou Ímpar ?
# Receba um número inteiro na entrada e imprima par ou ímpar

resto = 0.00

numero = input("Entre com o um número inteiro: ")

resto = int(numero)%2
if resto == 0 :
  print('par')
else :
  print('impar')

