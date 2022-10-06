# Exercício 2 - Primos
# Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e devolve o maior número primo menor ou igual ao número passado à função
#
# Dica: escreva uma função éPrimo(k) e faça um laço percorrendo os números até o número dado checando se o número é primo ou não; se for, guarde numa variável.
# Ao fim do laço, o valor armazenado na variável é o maior primo encontrado.

def eprimo(k):

  n = 2
  numero = 0

  if k<2:
    return "Teste: Não é possivel calcular"
  else:
    while n<=k:
      if all(n%x != 0 for x in range(2,n)): # n(começa em 2 e vai até chegar no k(número digitado)) e divide com x (que vai de 2 até n-1, porque o stop não conta) e se todos os restos, nesse range, for diferente de 0, faça:
        numero=n
        n=n+1
      else:
        n=n+1

  return numero

k=int(input("numero k:"))

print(eprimo(k))