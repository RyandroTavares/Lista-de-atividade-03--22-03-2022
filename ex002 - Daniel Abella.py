# 02 Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo

valor = int(input('Digite um valor: '))
print()

if valor > 0:
  print('Valor é positivo!')

elif valor < 0:
  print('Valor é negativo')
  
else:
  print('Valor é nulo!')