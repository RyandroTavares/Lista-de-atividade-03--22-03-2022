# 04 Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = str(input('Digite uma letra: ')).lower()
vogal = 'aeiou'
cosoante = 'bcdfjklmnpqrstvwxyz'
print()

if letra in vogal:
  print('A letra é uma Vogal!')

elif letra in cosoante:
  print('A letra é uma Cosoante!')

else:
  print('Não é uma letra')