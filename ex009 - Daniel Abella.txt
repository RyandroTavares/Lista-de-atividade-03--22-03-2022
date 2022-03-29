# 09 Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N-Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

turno = str(input('Digite o seu turno: ')).upper()
print()

if turno == 'M':
  print('Bom dia Senhor(a)')
  print('O seu turno é Matutino!')

elif turno == 'V':
  print('Boa tarde Senhor(a)')
  print('O seu turno é Vespertino!')

elif turno == 'N':
  print('Boa noite Senhor(a)')
  print('O seu turno é Noturno!')

else:
  print('Não é um turno válido!')