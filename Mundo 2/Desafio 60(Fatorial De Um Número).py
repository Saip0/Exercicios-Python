#Um Programa Simples Apenas Para Treinar A Lógica
while True:
    try:
        num1 = int(input("Numero:"))
    except ValueError:
        print("Valor invalido")
        continue
    fact = 1
    for i in range(1,num1+1):
        fact *= i

    print(fact)
