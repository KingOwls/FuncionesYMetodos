
def Operaciones(n1,n2,op="+"):
    if(op=="+"):
        print(f"la suma de los nros es = {n1+n2}")
    elif(op=="-"):
        print(f"la resta de los nros es = {n1-n2}")

def resta(a,b):
    print(a-b)
resta(10,8)

def restaA(a,b, C=0):
    #Resta multiplicando
    if C>=0:
        print((a-b)*C)
    #Resta sin multiplicar
    else:
        print(a-b)

#Resta sin multiplicar
restaA(10,8)

#Resta multiplicando
restaA(10,8,8)

#Metodo listas
def verLista(Lista):
    for item in Lista:
        print(item,end=" ")
verLista(["Rojo"], ["Azul"])

#Contenido de una lista
def verListas(**Lista):
    for key,valor in Lista.items():
        print(f"{key} : {valor}", end="\n")

diccionario={
    "Nombre": "Jose M",
    "Edad": 14
}
verListas(**diccionario)

#Suma
def suma(a,b):
    return a+b
print(suma(3,4))

#Sentencia de un retun
def Division(numerador, dividendo):
    if dividendo==0:
        return
    else:
        return numerador/dividendo

resultado=Division(3,0)
if resultado!= None:
    print(resultado)
else:
    print("No se puede dividir por cero")

def DivisionB(numerador, dividendo):
    if dividendo==0:
        return 
    else:
        return numerador/dividendo
restado=DivisionB(8,3)

if restado!= None:
    print(restado)
else:
    print("No se puede dividir por cero")

def divisionC(numerador, dividendo):
    if dividendo==0:
        return None
    else:
        return numerador/dividendo
print(divisionC.doc_)
resultado=divisionC(8,3)

if resultado!= None:
    print(resultado)
else:
    print("No se puede dividir por cero")
def multipicacion(a:int, b:int)->int:
    return a*b
print(multipicacion(3,5))

dato=10
def estado(x):
    x=20
estado(dato)
print(dato)

#*args y **kwargs
def valores(*args):
    for i in args:
        print(f"{i}", end=" ")
valores(1,2,3,4,5)