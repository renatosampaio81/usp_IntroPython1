# Exercício 1
# Faça um programa em Python que receba (entrada de dados) o valor correspondente ao lado de um quadrado, calcule e imprima (saída de dados) seu perímetro e sua área.
#
# Observação: a saída deve estar no formato: "perímetro: x - área: y"

lado = input("Entre com o valor do lado do quadrado (em cm): ")

area = int(lado) ** 2
perimetro = int(lado) * 4

print('perímetro: ', perimetro, ' - área: ', area)