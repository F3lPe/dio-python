#nos métodos a indentação é obrigatória

LIMITE_SAQUE = 1000
saldo = 10000

def sacar(valor):
    if valor <= LIMITE_SAQUE:
        print("Valor Sacado!")
        print(f"Saldo disponível: {saldo - valor}")

    #else if -> elif
    elif valor > saldo:
        print("Valor para saque insuficiente")
    else:
        print(f"Limite para saque insuficiente. O limite é de {LIMITE_SAQUE}")

sacar(2)

def depositar(valor):
    global saldo
    saldo += valor

    return saldo

total = depositar(200)
print(total)

number = 10

#ternário
print("É 10" if number >= 10 else "não é 10")

#estruturar de repetição

listaNomes = ["felippe", "ana", "Carol"]

for nome in listaNomes:
    print(nome)
else:
    print("dwadwa")

numero = 0

while numero <= 1:
    numero = int(input("numero: "))
    print(numero)