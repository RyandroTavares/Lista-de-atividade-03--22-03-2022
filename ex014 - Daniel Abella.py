# 14 Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
# O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# • Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# • Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

print('Podera ser sacado no mínimo R$ 10,00 reais e no máximo R$ 600,00')
valor = int(input('Digite o valor do saque: R$ '))
nota100 = 0
nota50 = 0
nota10 = 0
nota5 = 0
nota1 = 0
print()

if valor >= 10 and valor <= 600:
  nota100 = valor // 100
  valor = valor % 100
  nota50 = valor // 50
  valor = valor % 50
  nota10 = valor // 10
  valor = valor % 10
  nota5 = valor // 5
  valor = valor % 5
  nota1 = valor // 1
  valor = valor % 1

  if nota100 != 0:
    nota100 = ('{} notas de 100').format(nota100)

  if nota50 != 0:
    nota50 = ('{} notas de 50').format(nota50)

  if nota10 != 0:
    nota10 = ('{} notas de 10').format(nota10)

  if nota5 != 0:
    nota5 = ('{} notas de 5').format(nota5)

  if nota1 != 0:
    nota1 = ('{} notas de 1').format(nota1)

  print('Para sacar a quantia precisa de {}, {}, {}, {} e {}'.format(nota100, nota50, nota10, nota5, nota1))

else:
  print('O valor digitado é menor que R$ 10,00 ou maior que R$ 600,00!')