# 12 Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.

data = input('Digite uma data no formato dd/mm/aaaa: ')
dia = int(data[:2])
mes = int(data[3:5])
ano = int(data[6:])
print()

if dia > 0 and dia < 32 and mes > 0 and mes < 13 and ano > 0 and ano < 2022:
  
  if dia > 0 and dia <= 31:
    dia = dia

  if mes > 0 and mes <= 12:
    mes = mes

  if ano > 0:
    ano = ano

  print('A data {}/{}/{} é Válida!'.format(dia, mes, ano))

else:
  print('A data informada é inválida!')
