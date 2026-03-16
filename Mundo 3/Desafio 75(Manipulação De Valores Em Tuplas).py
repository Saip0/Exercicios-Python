def nums(num_rang):
    tupl:tuple = ()
    cont = 0
    for i in range(0,num_rang):
        num:int = (int(input(f'Num{i+1}:')),)
        tupl += num
        if tupl[i]%2 == 0:
            cont += 1
    return tupl,cont

def tupl_3numb(tupl):
    for t in tupl:
        if t == 3: 
            return tupl.index(3)+1
    else: 
        return '3 Not In Tuple'
        
while True:
    try:
        num_rang:int = int(input("Number For Range:"))
        tupl,cont_p = nums(num_rang)
    except ValueError:
        print("ERR")
        continue

    print(f"Digited Numbers: {tupl}\n"
    f"Pars Numb:{cont_p}")
    
    if tupl.count(9) == 0:
        print("Nine Not Surg")
    else:
        print(f"Nine Surg: {tupl.count(9)}X")
    
    if isinstance(tupl_3numb(tupl),int):
        print(f"Theer Value In Pos:{tupl_3numb(tupl)}")
    else:
        print(tupl_3numb(tupl))
    
    while True:
        ext:str = str(input("Think About Exit?:[Y,N]")).upper().strip()[0]
        if ext in ['Y,','N']: break
        else:
            print('Err')
            continue
    if ext == 'Y': break    