lista = ['a', 'b', 'c', 'd', 'e', 'f']
lista_strings_maiusculas = list(map(lambda x: x.upper(), lista))
print(lista_strings_maiusculas)


lista_palavras = ["banana", "maçã", "laranja", "abacaxi", "uva", "morango"]

palavras_com_mais_de_5_letras = list(filter(lambda x: len(x) > 5, lista_palavras))

print(palavras_com_mais_de_5_letras)

# from functools import reduce

lista_numeros = [10, 5, 8, 13, 2, 6]

valor_maximo = reduce(lambda x, y: x if x > y else y, lista_numeros)

print(valor_maximo)


# 4
lista_pessoas = [
    {"nome": "João", "idade": 25},
    {"nome": "Maria", "idade": 30},
    {"nome": "Pedro", "idade": 40}
]

nomes_pessoas = list(map(lambda pessoa: pessoa["nome"], lista_pessoas))

print(nomes_pessoas)