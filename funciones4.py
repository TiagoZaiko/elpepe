#Funciones
def conversion_notas (puntaje,puntaje_total):
    nota=(puntaje*6/puntaje_total)+1
    
    return round(nota,1)

#Codigo Principal
while True:
    try:
        p=float(input("ingrese la nota del estudiante"))
        if p< 0:
            print ("debe ser una nota positiva")
        else:
            break
    except ValueError:
        print("debe ingresar un numero")
while True:
    try:
        pt=float(input("ingrese la nota total de la evaluacion"))
        if pt<0:
            print("debe ser una nota positiva")
        else:
            break
    except ValueError:
        print("Debe ingresar un numero")
calif=conversion_notas(p,pt)
print(f"la nota chilena es {calif}")