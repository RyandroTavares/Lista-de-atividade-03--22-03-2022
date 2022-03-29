# 07 Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.

produto1 = float(input('Valor produto 1: R$ '))
produto2 = float(input('Valor produto 2: R$ '))
produto3 = float(input('Valor produto 3: R$ '))
print()

if produto1 < produto2 and produto1 < produto3:
  print('O produto com o valor de \033[33mR$ {}\033[m é mais barto!'.format(produto1))

elif produto2 < produto1 and produto2 < produto3:
  print('O produto com o valor de \033[33mR$ {}\033[m é mais barato!'.format(produto2))

else:
  print('O produto com o valor de \033[33mR$ {}\033[m é o mais barato!'.format(produto3))