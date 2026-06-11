def mostrar_encabezado():
    print("---------------------------")
    print("sistema de admision escolar")
    print("---------------------------")  


def solicitar_datos():
    estudiantes = {}
    estudiantes["rut"] = input("ingrese el rut del estudiantes: ")
    estudiantes["nombre"] = input ("ingrese el nombre del estudiante: ")
    estudiantes["carrera"] = input("ingrese la carrera que estudia: ")
    while True:
        try:
            estudiantes["semestre"] = int(input("ingrese el semestre que cursa: "))
            if estudiantes ["semestre"] < 1 or estudiantes["semestre"] >4:
                print("debe ser del 1 al 4")
            else:
                break
        except ValueError:
            print("debe ingresar un numero ")
    return estudiantes

def mostrar_datos(alumnos):
    print(f"nombre del estudiante: {alumnos["nombre"]}")
    print(f"rut del estudiante: {alumnos["rut"]}")
    print(f"carrera del estudiante: {alumnos["carrera"]}")
    print(f"semestre del estudiante: {alumnos["semestre"]}")

datos=solicitar_datos()
mostrar_encabezado()
mostrar_datos(datos)