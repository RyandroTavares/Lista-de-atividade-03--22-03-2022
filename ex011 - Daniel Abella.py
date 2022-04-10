# 11 Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.

ano = int(input('Digite o ano: '))
anobissexto = ano % 4
print()

if anobissexto == 0:
  print('O ano é bissexto!')

else:
  print('O ano não é bissexto')