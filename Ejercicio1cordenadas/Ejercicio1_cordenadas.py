"""Ejercicio 1
Programa que lea las coordenadas cartesianas (x, y) de un punto en el plano y calcula el cuadranteal cual pertenece el punto."""

print("------------------------------")
print("---coordenadas cartesianas----")
print("------------------------------")

#input
x=int(input("Ingrese el valor de x: "))
y=int(input("ingrese el valor de y: "))

#processing
if x>=0 and y>=0:
    print("las coordenadas: " + "(" +str(x)+"," + str(y) +")" +" se encuentra en el CUADRANTE 1.")
else:
        if x<=0 and y>=0:
             print("las coordenadas: " + "(" +str (x)+"," + str(y) + ")" + " se encuentra en el CUADRANTE 2.")
        else: 
             if x<=0 and y<=0:
                 print("las coordenadas: " + "(" +str (x)+"," + str(y) + ")" + " se encuentra en el CUADRANTE 3.")
             else:
                if x>=0 and y<=0:
                      print("las coordenadas: " + "(" +str(x)+"," + str(y) + ")" + " se encuentra en el CUADRANTE 4.")