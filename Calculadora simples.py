#pegar dois números e efetuar mostrando na tela
#a soma, divisão, multiplicação e subtração da seguinte maneira
#exemplo:
# A soma dos dois números é: SOMA

n1 = int(input("Digite o primeiro numero : "))
n2 = int(input("Digite o segundo numero :"))
soma = n1+n2
divisao = n1/n2
#multiplicacao = n1*n2
#subtracao = n1-n2
print("O resultado da soma é : ", soma)
#print("resultado da Soma é : ", n1+n2)
print("resultado da Subtração é : ", n1-n2)
print("resultado da Divisão é : ", n1/n2)
print(type(divisao))
print("resultado da Multiplicação é : ", n1*n2)