mitupla =(1,2,3,4,5)
print(type(mitupla))


tuplaCiudades = "Buc", "Cal", "Bog"
print(tuplaCiudades)
CiuTemp = list (tuplaCiudades)
CiuTemp [0] = "Cuc"
tuplaCiudades = tuple (CiuTemp)
CiuTemp = list(tuplaCiudades)
print(tuplaCiudades)
print(f"Total de ciudades {tuplaCiudades.count('Cuc')}")
print(f"Indice Bog {tuplaCiudades.index('Bog')}")
