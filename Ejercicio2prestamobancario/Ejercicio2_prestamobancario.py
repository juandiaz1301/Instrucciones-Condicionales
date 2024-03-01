# Programa para verificar si un prestamo puede ser consolidado segun el salario o deudas de la persona

# input
Salario= int(input("cuanto es su salario : "))
Deuda= int(input("usted tiene otra deuda que no ha pagado(si o no) : "))

# Procesing
if Salario >= 945200:
    if Deuda == "no":
        print ("Su prestamo a sido aprobado")
else:
    print ("Su prestamo a sido denegado")        
        