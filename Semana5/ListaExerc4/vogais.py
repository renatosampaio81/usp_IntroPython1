# Exercício 3 - Vogais
# Escreva a função vogal que recebe um único caractere como parâmetro e devolve True se ele for uma vogal e False se for uma consoante.
#
# Dica: Lembre-se que para passar uma vogal como parâmetro ela precisa ser um texto, ou seja, precisa estar entre aspas.

def vogal(v):
  if (v == "a" or v == "e" or v == "i" or v == "o" or v == "u" or v == "A" or v == "E" or v == "I" or v == "O" or v == "U") :
    return True
  else :
    return False

v=input("ente com uma vogal: ")

print(vogal(v))