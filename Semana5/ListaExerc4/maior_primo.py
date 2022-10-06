def maior_primo(k):

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