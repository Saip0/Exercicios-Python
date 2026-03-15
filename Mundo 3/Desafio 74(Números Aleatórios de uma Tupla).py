from random import randint
spc = {15 : '='*15,
       50 : '='*50}

def som_tuple(numb_loop):
    tupl:tuple = ()
    for i in range(0,numb_loop):
        num_ramdom:tuple = (randint(0,100),)
        tupl += num_ramdom
    return tupl

err = f"{spc[15]}Err{spc[15]}"

while True:
    try:
        numb_loop:int = int(input(f'{spc[50]}\nNumbLoop:'))
    except ValueError:
        print(err)
        continue
    def_tuple = som_tuple(numb_loop)
    print(f"The Values Sortes: {def_tuple}\n"
          f"The Max Number Is {max(def_tuple)} \n"
          f"The Min Number Is {min(def_tuple)}")
    while True:
        ext:str = str(input(f'{spc[50]}\n'
                            'Think About Leave?[Y,N]')).upper().strip()[0]
        if ext in ['Y','N']:    break
        else:
            print(err)
            continue
    if ext == 'Y':  break