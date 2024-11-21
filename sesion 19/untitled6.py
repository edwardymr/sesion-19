n = int(input("Cuántos puntos quiere procesar?"))

primer_cuadrante = 0
segundo_cuadrante = 0
tercer_cuadrante = 0
cuarto_cuadrante = 0


for i in range (n):
    print("punto", i + 1)
    x = int(input("Ingrese la coordenada x del punto: "))
    y = int(input("Ingrese la coordenada y del punto: "))
    
    if x > 0 and y > 0:
        primer_cuadrante += 1 
    elif x < 0 and y > 0:
        segundo_cuadrante += 1
    elif x < 0 and y < 0:
        tercer_cuadrante += 1 
    elif x > 0 and y < 0:
        cuarto_cuadrante += 1 
        
print("Puntos en el Primer cuadrante", primer_cuadrante)
print("Puntos en el Segundo cuadrante", segundo_cuadrante)
print("Puntos en el Tercer cuadrante", tercer_cuadrante)     
print("Puntos en el Cuarto cuadrante", cuarto_cuadrante) 