#escopo / variavel global
x = "Senac"
#variavel global. Criada fora do escopo Mostrar 
def Mostrar():
    print(x)
Mostrar()

x = "jose"

def MostrarNome():
    x = "SENAC"
    print(x)

MostrarNome()
print(x)
#variavel criada para diferenciar nome dentro do mesmo contexto. Alterando a informação a partir da posição do comando