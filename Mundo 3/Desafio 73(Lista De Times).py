#data 2026
teams:tuple = (
    "São Paulo","Palmeiras","Fluminense","Bahia","Bragantino","Flamengo","Coritiba","Athletico-PR",
    "Grêmio","Corinthians","Mirassol","Chapecoense","Atlético-MG","Santos","Vasco","Vitória","Botafogo",
    "Remo","Internacional","Cruzeiro"
)
spc:dict = {15 : '='*15,
            50 : '='*50}

def opts(option,err):
    if option in [1,2,3,4]:
        if option == 1: return teams[:4]
        elif option == 2: return teams[-4:]
        elif option == 3: return sorted(teams)
        elif option == 4:
            want_team:input = str(input("Name Team:"))
            if want_team in teams:
                return want_team,teams.index(want_team)
            else:   return "Not In List"
    else:
        return err
err = f"{spc[15]}Err{spc[15]}"

while True:
    try:
        option:input = int(input(f"{spc[50]}\nOption:"))
    except ValueError:
        print(err)
        continue
        
    pross_option = opts(option,err)
    if isinstance(pross_option[0],str) and isinstance(pross_option[1],int):
        team, index_team = pross_option
        print(f"Team:{team}\n"
              f"In Position:{index_team+1}")
    elif isinstance(pross_option,tuple):
        print("List Teams:\n"
              f"{'\n'.join(pross_option)}")
    elif isinstance(pross_option,list):
        print(f"List In Alphabetical Order:\n"
              f"{"\n".join(pross_option)}")
    else:
        print(pross_option)
        
    while True:
        ext:input = str(input(f"{spc[50]}\nThink About Exit?[Y/N]")).upper().strip()[0]
        if ext in ['Y','N']:    break
        else:
            print(err)
            continue
    if ext == 'Y':  break