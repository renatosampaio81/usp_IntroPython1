# Exercício 1
# Escreva um programa que receba um número natural  n n na entrada e imprima  n! n! (fatorial) na saída.
#
# Dica: lembre-se que o fatorial de 0 vale 1!

def factorial(n) :
  return 1 if (n==1 or n==0) else n * factorial(n-1)

n = int(input("Digite o valor de n: "))
print (factorial(n))
