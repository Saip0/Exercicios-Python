from random import randint

esp = {15 :'='*15,
       50 :'='*50}
aleat_num = randint(0, 10)
cont = 0
def numero_aleatorio(aleat_num ,numero):
    if numero < aleat_num:
        return 1
    elif numero > aleat_num:
        return  2
    else:
        return 3

err = f"{esp[15]}ERRO{esp[50]}"
while True:
    try:
        numero = int(input(f"{esp[50]}\nNúmero:"))
    except ValueError:
        print(err)
        continue
    if -1 < numero < 11:
        pass
    else:
        print(err)
        continue
    resultado = numero_aleatorio(cont,aleat_num,numero)
    if resultado in [1,2]:
        if resultado == 1:
            print(f"O Número é maior que {numero}")
            cont += 1
        else:
            print(f"O Número é menor que {numero}")
            cont += 1
    else:
        print(f"Fim De Jogo, O Número Era {numero}\n"
              f"Você Precisou De {cont} Tentivas")

        while True:
            sair = str(input(f"{esp[50]}\nDeseja Sair?[S/N]:")).strip().upper()[0]
            if sair in ['S','N']:
                break
            else:
                print(err)
        if sair == 'S':
            break
        aleat_num = randint(0, 10)

        cont = 0
