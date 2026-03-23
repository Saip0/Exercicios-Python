list_num:list = []
esp:dict = {15 : '='*15,
                   50 : '='*50}

def armz_list(list_num,quantidade_de_valores):
    i = 0
    while i<=quantidade_de_valores:
        try:
            valores:int = int(input(f'Valor Da Posição{i+1}:'))
        except ValueError:
            print("ERR")
            i-1
            continue
        i += 1
        list_num.append(valores)
    return max(list_num),min(list_num)

while True:
    try:
        quantidade_de_valores:int = int(input(f'{esp[50]}\n'
                                              'Quantidade De Valores:'))
        max_list, min_list = armz_list(list_num,quantidade_de_valores)
    except ValueError:
        print("ERR")
        continue
    
    print(f"Da Lista: {' ,'.join(map(str,list_num))}\n"
          f"O Maior Valor é: {max_list}\n"
          f"E O Menor Valor é: {min_list}")
    
    while True:
        sair:str = input("Sair?[S/N]:").upper().strip()[0]
        if sair in 'SN': break
        else: print("ERR")
    if sair == 'S': break