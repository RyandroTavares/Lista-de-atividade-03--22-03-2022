# 16 Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

numero = float(input('Digite um número: '))
print()

if numero % 1 == 0:
  print('Número é inteiro!')

else:
  print('Número é decimal!')