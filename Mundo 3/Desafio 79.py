list_valors:list = []
def adicionar_valores(list_valors,valor):
    if valor not in list_valors:
        return list_valors.append(valor)
    else:
        return False

while True:
    try:
        valor:int = int(input('Digite Um Número'))
    except ValueError:
        print(f"Err{'='*15}")
    
    if adicionar_valores(list_valors,valor) is False:
        print("Esté Número Já Existe Na Lista")
    else:
        print(f"O Valor {valor} Foi Adicionado Na Lista")
        
    while True:
        sair:str = str(input("Sair[S/N]")).upper().strip()[0]
        if sair in 'SN': break
        else: 
            print(f"Err{'='*15}")
            continue
    if sair == 'S': 
        print(f"{'-='*25}\n"
              f"Você Digitou Os Valores {', '.join(map(str,list_valors))}")
        break