#Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

#a=input("Digite o primeiro numero: ")
#b=input("Digite o segundo numero: ")

#resultado=int(a) * int(b)
#print(f"o resultado da multiplicacao é: {resultado}")


#Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

# a=input("digite o proimeiro numero inteiro: ")
# b= input("digite o segundo nunmero inteiro: ")
# resultado= float(a)//float(b)

# print(f"o resultado da divisão inteira é: {resultado}")4

#Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

# a=input("digite o numiero para calcular o quadrado:")
# resultado =float(a)**2

# print(f"o quadrado de {a} é: {int(resultado)}")


# joao 


a=str(input("difite uma string: "))
b=str(input("digite outra string: "))

try:    
    if not a or not b:
        print("Strings não podem ser vazias")
    else:
        print(f"concatenação das strings: { a + b }")
except NameError:
    print("Valor inválido, digite uma string.")