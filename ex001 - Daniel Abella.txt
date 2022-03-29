# 01 Faça um Programa que peça dois números e imprima o maior deles.

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
print()

if numero1 > numero2:
  print('O número {} é maior que o número {}'.format(numero1, numero2))

else:
  print('O número {} é maior que o número {}'.format(numero2, numero1))