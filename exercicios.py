import math

#Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

a=float(input( "Digite o primeiro número inteiro: "))
b=float(input( "Digite o segundo número inteiro: "))

print(a//b)



# Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

a=float(input("Digite o valor do raio do círculo: "))
areacirculo= math.pi * (a**2)
print(f"area do circulo é:{areacirculo:.2f}")