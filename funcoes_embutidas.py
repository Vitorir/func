lista = ['a', 'b', 'c', 'd', 'e', 'f']
lista_strings_maiusculas = list(map(lambda x: x.upper(), lista))
print(lista_strings_maiusculas)


lista_palavras = ["banana", "maçã", "laranja", "abacaxi", "uva", "morango"]

palavras_com_mais_de_5_letras = list(filter(lambda x: len(x) > 5, lista_palavras))

print(palavras_com_mais_de_5_letras)