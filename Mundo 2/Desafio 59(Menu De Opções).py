esp = {15 : '='*15,
       50 : '='*50}

def calcular(err,numero1,numero2):
    opcao = int(input("O Que Você Quer Fazer Com Os Valores?\n"
                      "[ 1 ] Somar\n"
                      "[ 2 ] Multiplicar\n"
                      "[ 3 ] Dividir\n"
                      "[ 4 ] Maior\n"
                      "[ 5 ] Novo Número\n"
                      "Opção:"))
    if opcao in [1,2,3,4,5]:
        if opcao == 1:
            soma = numero1 + numero2
            return soma
        elif opcao == 2:
            multiplicar = numero1 * numero2
            return multiplicar
        elif opcao == 3:
            dividir = round(numero1 / numero2,2)#arredonda o número
            return dividir
        elif opcao == 4:
            maior = max(numero1,numero2)
            return maior
        else:
            numero1 = int(input("Digite O Primeiro Número:"))
            numero2 = int(input("Digite O Segundo Número:"))
            return numero1, numero2
    else:
        return err
numero2 = None
err = f"{esp[15]}ERR{esp[15]}"
while numero2 is None:
    try:
        numero1 = int(input("Digite O Primeiro Número:"))
        numero2 = int(input("Digite O Segundo Número:"))
    except ValueError:
        print(err)
        continue

while True:
    try:
        resultado = calcular(err,numero1, numero2)
        if isinstance(resultado, tuple):#verifica o o tipo de resultado retornado, se for tupla acontece a ação
            numero1, numero2 = resultado
        else:
            print(resultado)
    except ValueError:
        print(err)
        continue
    while True:
        sair = str(input(f"{esp[50]}\nDeseja sair? [S/N]")).upper().strip()[0]
        if sair in ["S","N"]:
            break
        else:
            print(err)
    if sair == 'S':
        break