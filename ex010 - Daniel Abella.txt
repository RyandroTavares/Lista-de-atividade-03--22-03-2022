# 10 Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2-Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

diadasemana = int(input('Digite um número de 1 a 7 para saber o dia da semana: '))
dia = 0
print()

if diadasemana >= 1 and diadasemana <= 7:
  dia = 0
  
  if diadasemana == 1:
    dia = 'Domingo'

  elif diadasemana == 2:
    dia = 'Segunda'

  elif diadasemana == 3:
    dia = 'Terça'

  elif diadasemana == 4:
    dia = 'Quarta'

  elif diadasemana == 5:
    dia = 'Quinta'

  elif diadasemana == 6:
    dia = 'Sexta'

  elif diadasemana == 7:
    dia = 'Sabado'

  print('O número {} corresponde a {}!'.format(diadasemana, dia))

else:
  print('O número {} não tem correspondente!'.format(diadasemana))