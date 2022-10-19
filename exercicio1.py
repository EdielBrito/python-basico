#1.	Elabore um programa em Python que leia a medida de um raio de um círculo e efetue o cálculo da sua área,
# exibindo o resultado ao final. (dica: use math.pi )

import math
raio = float(input("Insira o valor do raio do círculo: "))
area = math.pi * ((raio)**2)
print("O cálculo da sua área é: {:.1f}." .format(area))
