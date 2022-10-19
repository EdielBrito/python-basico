#4.	Faça um programa que calcule o fatorial de um número positivo informado pelo usuário.

n = int(input("Digite um número positivo: "))
fatorial = 1
print(f"{n}! =", end="")
for c in range(n, 0, -1):
    print(f"* {c}", end="")
    fatorial = fatorial * c
print(f" = {fatorial}")
