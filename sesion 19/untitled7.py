ciudades = {
    "Bogota": 18,
    "Cartagena": 30,
    "Medellin": 24,    
}
ciudad_min = min(ciudades, key=ciudades.get)
temperatura_min = ciudades[ciudad_min]

print("La ciudad con la temperatura mas baja es:", ciudad_min)
print("Temperatura promedio:", temperatura_min)