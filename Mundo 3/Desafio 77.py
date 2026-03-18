palavras:tuple = ("casa", "livro", "janela", "carro", "tempo")

for letras in palavras:
    letras = letras.upper()
    print(f"Na Palavra {letras} Temos ", end= ' ')
    for letra in letras:
        if letra in 'AEIOU':
            print(letra.lower(), end=' ')
    print()