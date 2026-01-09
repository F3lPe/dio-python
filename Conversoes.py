preco1, preco2 = 10, 2
DESCONTO = 2
PRECO_COM_DESCONTO = (preco1 + preco2) * (DESCONTO / 100)
PRECO_FINAL = preco1 + preco2 - PRECO_COM_DESCONTO

print(PRECO_FINAL)

print(type(int(PRECO_FINAL)))
print(int(PRECO_FINAL))

print(type(str(PRECO_FINAL)))
print(str(PRECO_FINAL))
