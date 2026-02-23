lista = ["laranja", "uva", 1.20, True]

letras = list("uva")

numeros = list(range(3))

matriz = [
    [1, "a"],
    ["Felipe", 2],
    ["Jao", 3]
]

# print(matriz[0][1])print(letras)
# print(numeros)
# print(letras[1])

for indicie, it in enumerate(lista):
    if type(it) is str:
        lista.append(10)
    else:
        print(it)
else:
    print("a lista está vazia")
    print(lista)

for numero in numeros:
    print(numero)