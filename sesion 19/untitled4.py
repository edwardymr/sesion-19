estudiante = {
    "nombre": "Juan",
    "edad": 25,
    "curso": "Python"
}

print(estudiante["nombre"])

estudiante["nota"] = 98
print(estudiante["nota"])

del estudiante ["curso"]
print(estudiante)


del estudiante ["edad"]
print(estudiante)