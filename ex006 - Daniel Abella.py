# 06 Faça um Programa que leia três números e mostre o maior e o menor deles.

numero1 = int(input('Primeiro número: '))
numero2 = int(input('Segundo número: '))
numero3 = int(input('Terceiro número: '))
menor = 0
maior = 0
print()

# Saber o maior número!
if numero1 > numero2 and numero1 > numero3:
  maior = numero1
  
elif numero2 > numero1 and numero2 > numero3:
  maior = numero2

else:
  maior = numero3

# Saber o menor número!
if numero1 < numero2 and numero1 < numero3:
  menor = numero1

elif numero2 < numero1 and numero2 < numero3:
  menor = numero2

else:
  menor = numero3

print('O maior número é {}!'.format(maior))
print('O menor número é {}!'.format(menor))