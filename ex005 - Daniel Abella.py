# 05 Faça um Programa que leia três números e mostre o maior deles.

numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))
numero3 = int(input('Terceiro número: '))
print()

if numero1 > numero2 and numero1 > numero3:
  print('O número {} é o maior!'.format(numero1))

elif numero2 > numero1 and numero2 > numero3:
  print('O número {} é o maior!'.format(numero2))

else:
  print('O número {} é o maior!'.format(numero3))