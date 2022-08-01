##############
#questão 01
def funcao(x):
    #utilizando o isistance ele compara o valor 
    #com o tipo escolhido 
    if isinstance(x,int):
        print(f'{x} é um inteiro')
    else:
        print("O numero tem que ser inteiro")
##############
#questão 03
#print("digite 3 icognitas e atribua 
# valores a elas")
def soma(x,y,z):
    operacao = x + y + z 
    return operacao
##############
#questão 51
import math
def coordenada(x,y):
    b=x**2
    c=y**2
    z=b+c
    a=pow(z,0.5)
    return a
