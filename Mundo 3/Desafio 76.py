list:tuple = ('Lápis',1.75,
              'Borracha',2,
              'Caderno',15,
              'Estojo',25,
              'Transferidor',4.20,
              'Compasso',9.99,
              'Mochila',120.32,
              'Canetas',22.30,
              'Lirvro',34.90)

print(f"{'-'*50}\n",
      f"{'Listagem De Preços'.upper().center(45)}\n"
      f"{'-'*50}")
for item in list:
    if type(item) == str:
        print(f"{item}",end=f"{'.'*(35 -len(item))}R${' '*2}")
    else:
        print(f"{item:.2f}")
print('-'*50)