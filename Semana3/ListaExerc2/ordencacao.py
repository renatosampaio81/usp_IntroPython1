# Exercício 5
# Receba 3 números inteiro na entrada e imprima "crescente" se eles forem dados em ordem crescente.
# Caso contrário, imprima "não está em ordem crescente"

def crescente(num1,num2,num3):
  if (num1<num2) and (num2<num3):
    print("crescente")
  else:
    print("não está em ordem crescente")

num1 = int(input("Entre com o primeiro número inteiro: "))
num2 = int(input("Entre com o segundo número inteiro: "))
num3 = int(input("Entre com o terceiro número inteiro: "))

crescente(num1,num2,num3)