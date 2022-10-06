# Exercício 3
# Escreva um programa que receba um número inteiro na entrada, calcule e imprima a soma dos dígitos deste número na saída.
# 
# Dica: Para separar os dígitos, lembre-se: o operador "//" faz uma divisão inteira jogando fora o resto, ou seja, aquilo que é menor que o divisor;
# O operador "%" devolve apenas o resto da divisão inteira jogando fora o resultado, ou seja, tudo que é maior ou igual ao divisor.

def somadig(n) :
  soma = 0

  while (n != 0):
    resto = n % 10
    n = (n - resto)//10
    soma = soma + resto

  print(soma)


n = int(input("Digite um número inteiro: "))
somadig(n)