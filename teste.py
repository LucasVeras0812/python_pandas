texto = "O Python é uma linguagem de programação poderosa e versátil. " \
"Aprender Python abre portas para diversas áreas, como ciência de dados, desenvolvimento web e automação. " \
"A prática constante é a chave para a maestria em qualquer linguagem."

texto = texto.lower()

contagem_palavras = {}
print(contagem_palavras)


palavras = texto.split()
print(palavras)

for palavra in palavras:
    palavra = palavra.strip('.,;:!?')
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print(palavras)

print("\nAs 3 palavras mais frequentes:")
palavras_mais_frequentes = sorted(contagem_palavras.items(), key=lambda x: x[1], reverse=True)[:3]

for palavra, quantidade in palavras_mais_frequentes:
    print(f'A palavra "{palavra}" aparece {quantidade} vez(es)')

print(f"\nTotal de palavras no texto: {len(palavras)}")