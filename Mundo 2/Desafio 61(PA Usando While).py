while True:#Gera Uma PA Usando While
    try:#Programa Simples Apenas Didadico
        termo = int(input("Termo"))
        razao = int(input("Razao"))
        break
    except ValueError:
        print("Erro")
        continue
contador = 0
while contador < 10:
    print(f"{termo} ➡", end=' ')
    termo += razao
    contador += 1
print("Fim")