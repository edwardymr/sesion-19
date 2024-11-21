n = int(input("Cuántas personas quieres procesar?"))

menores = 0
mayores = 0
total_edades = 0

i=0

while i < n:
    edad = int(input("Ingrese la edad de la persona:" + str(i + 1) + ": "))
    total_edades = total_edades + edad
    if edad < 18:
        menores = menores + 1
    else:
        mayores = mayores + 1
    i += 1
print("total mayores", mayores)
print("total menores", menores)
print("total acumulado", total_edades)