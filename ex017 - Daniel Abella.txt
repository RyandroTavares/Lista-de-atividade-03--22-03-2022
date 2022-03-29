# 17 Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
# • par ou ímpar;
# • positivo ou negativo;
# • inteiro ou decimal.

numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
par1 = numero1 % 2
par2 = numero2 % 2
print()

# Saber se é Par ou Ímpar (numero1)!
if par1 == 0:
  numero1 = int(numero1)
  print('O número {} é Par!'.format(numero1))

else:
  numero1 = int(numero1)
  print('O número {} é Ímpar!'.format(numero1))

# Saber se é Par ou Ímpar (numero2)!
if par2 == 0:
  numero2 = int(numero2)
  print('O número {} é Par!'.format(numero2))

else:
  numero2 = int(numero2)
  print('O número {} é Ímpar!'.format(numero2))
print()


# Saber se é Positivo e Negativo (numero1)!
if numero1 > 0:
  print('O número {} é Posito!'.format(numero1))

elif numero1 < 0:
  print('O número {} é Negativo!'.format(numero1))

else:
  print('O número {} é Nulo!'.format(numero1))

# Saber se é Positivo e Negativo (numero2)!
if numero2 > 0:
  print('O número {} é Posito!'.format(numero2))

elif numero2 > 0:
  print('O número {} é Negativo!'.format(numero2))

else:
  print('O número {} é Nulo!'.format(numero2))
print()


# Saber se é Inteiro ou Decimal (numero1)!
if numero1 % 1 == 0:
  print('O número {} é Inteiro!'.format(numero1))

else:
  print('O número {} é Decimal!'.format(numero1))

# Saber se é Inteiro ou Decimal (numero2)
if numero1 % 1 == 0:
  print('O número {} é Inteiro!'.format(numero2))

else:
  print('O número {} é Decimal!'.format(numero2))