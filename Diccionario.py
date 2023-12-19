#Inicio de un diccionario
d1={
    "Nombre": "Camilo",
    "Edad": 25,
    "Documento": "12345"
}
#Impresion de un diccionario
print(d1)
#Cambio de un diccionario
d1['Nombre'] = "Pedro"
print(d1)

print(d1['Nombre'])
#Metodo de impresion de un diccionario
    #parametro de un diccionario
for item in d1:
    print(item)
    #cotenido de un diccionario
for key in d1:
    print(d1[key])
    #Impresion de parametro y contenido de un diccionario
for key, valor in d1.items():
    print(f"key:[{key}] valor:[{valor}]")
#Metodo de limpieza
d1.clear()
print(d1)
#Obtener de un parametro especifico
print(d1.get('Nombre'))
print(d1.get('Email', 'El correo no existe'))

lstD1 = d1.items()
print(lstD1)
print(list(lstD1))
print(list(lstD1)[0][0])

keys=d1.keys()
valores=d1.values()
print(list(keys))
print(list(valores))

d1.pop('Edad')
print(d1)

d2={
    "Nombre": "Camilo",
    "Edad": 25,
    "Documento": "12345",
    "Email" : "Camilo@gmail.com"
}

d1.pop('Nombre')
d1.update(d2)
print(d1)
