# Exercício 1 - Máximo
# Escreva a função maximo que recebe 2 números inteiros como parâmetro e devolve o maior deles.

def maximo(n1,n2):
  return n1 if (n1 > n2) else n2

n1 = int(input("Digite o primeiro número inteiro: "))
n2 = int(input("Digite o segundo número inteiro: "))

print (maximo(n1,n2))