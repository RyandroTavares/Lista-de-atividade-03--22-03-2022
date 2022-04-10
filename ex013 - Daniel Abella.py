# 13 Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
# • Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
# • 326 = 3 centenas, 2 dezenas e 6 unidades
# • 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310, 305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

valor = int(input('Digite um valor menor que 1000: '))
centena = valor // 100 % 10
dezena = valor // 10 % 10
unidade = valor // 1 % 10
print()

if valor >= 100:
  print('\033[4;96m{}\033[m = \033[1;32m{}\033[m Centenas, \033[1;32m{}\033[m dezenas e \033[1;32m{}\033[m unidades!'.format(valor, centena, dezena, unidade))

elif valor >= 10 and valor < 100:
  print('\033[4;96m{}\033[m = \033[1;32m{}\033[m dezenas e \033[1;32m{}\033[m unidades!'.format(valor, dezena, unidade))

elif valor >= 0 and valor < 10:
  print('\033[4;96m{}\033[m = \033[1;32m{}\033[m unidades!'.format(valor, unidade))
  