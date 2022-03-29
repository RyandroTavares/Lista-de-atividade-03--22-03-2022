# 03 Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F -Feminino, M -Masculino, Sexo Inválido.

sexualidade = str(input('Digite o seu sexo: ')).upper()
print()

if sexualidade == 'M':
  print('Masculino!')

elif sexualidade == 'F':
  print('Feminino!')

else:
  print('Sexo inválido!')