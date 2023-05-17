a = int(input('digite um número:'))
b = int(input('digite outro número:'))

def soma (a, b):
    print ("a soma de "+str(a)+" + "+str(b)+" é igual:" +str(a+b))
def subtração (a, b):
    print ("a subitração de "+str(a)+" - "+str(b)+" é igual:" +str(a-b))
def multiplicação (a, b):
    print ("a mutiblicacão de "+str(a)+" * "+str(b)+" é igual:" +str(a*b))
def divisão (a , b):
    print ("a divisão de "+str(a)+" / "+str(b)+"  é igual a:" +str(a/b))

ação = int(input('escolha a operaçaõ que será usado 1, 2, 3, 4:'))
       
if ação==1:
    soma(a,b)
if ação==2:
    subtração(a,b)
if ação==3:
    multiplicação(a,b)
if ação==4:
    divisão(a,b)


#pedir o número
#pedir a operação
#validar
#resposta do calculo





#inicia função
#da um nome
#envia os parametros
#cria o codigo