#6.	Elaborar um programa que solicita a entrada de 3 valores (a, b, c)
# e verifica se esses valores podem formar ou não um triângulo...

a = int(input("Digite um valor, por gentileza: "))
b = int(input("Digite um valor, por gentileza: "))
c = int(input("Digite um valor, por gentileza: "))
if a > 0 and b > 0 and c > 0:
    if a < b + c and b < a + c and c < a + b:
        print("Os valores formam um triângulo.")
        perimetro = a + b + c
        print(f"O perímetro desse triângulo é: {perimetro}.")
    else:
        print("Os valores não formam um triângulo!")
else:
    print(" Os valores não formam um triângulo!")
