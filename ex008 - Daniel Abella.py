# 08 Faça um Programa que leia três números e mostre-os em ordem decrescente.

numero1 = int(input('digite o primeiro numero: '))
numero2 = int(input('digite o segundo numero: '))
numero3 = int(input('digite o terceiro numero: '))
print()

numero = [numero1, numero2, numero3]
numero.sort(reverse=True)
print(numero)
