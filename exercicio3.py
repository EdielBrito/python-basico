#Escreva um programa que imprima todos os números pares
#compreendidos entre 85 e 907. O programa deve também calcular a
#soma destes valores

num = 86
soma = 0
while num <= 906:
    print(num)
    soma = soma + num
    num += 2

print("A soma de todos os números pares entre 85 e 907: {}".format(soma))
