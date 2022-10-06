# Exercício 2
# Receba um número inteiro positivo na entrada e imprima os  n n primeiros números ímpares naturais.
# Para a saída, siga o formato do exemplo abaixo.

def impares(n) :
  i = 0

  while n > i:
    print (2*i + 1)
    i = i + 1


n = int(input("Digite o valor de n: "))
impares(n)