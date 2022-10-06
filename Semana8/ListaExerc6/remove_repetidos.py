def remove_repetidos(lista):
  lista.sort()
  newList = []
  for x in lista:
    if x not in newList:
      newList.append(x)
  return newList

#lista = [2, 4, 2, 2, 3, 3, 1]
#print(remove_repetidos(lista))
