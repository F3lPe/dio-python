#operadores lógicos
valor1, valor2, valor3 = 10, 11, 20
nome1, nome2 = "1", 1

print("operadores lógicos:")
print(valor1 <= 10 or valor2 == 1)
print(valor1 == 10 and valor2 == 1)

#not é o operador de negação "!"

if not (valor2 > valor1) : print("valor2 é menor que valor1")
if not (valor2 > valor1) or valor3 == 20: print("hello world \n")

#operador de identidade - usado para descobrir se ocupam a mesma região de memória
print("operador de identidade:")
print(f"{nome1 is nome2} \n")

#operador de associação - usado para verificar se um objeto está presente em uma sequência
curso = "Python da DIO"
nomes = ["felipe", "ana", "lucas"]
saques = [1200, 10]

print("operador de associação:")
print("thon" in curso)
print("felipe" in nomes)
print(10 in saques)
