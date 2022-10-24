from animales import *
select=0
while(True):
    select=input("\n||------------------------||\n|| Selecciona una opcion: ||\n||------------------------||\n|| 1: Agregar             ||\n|| 2: Buscar              ||\n|| 3: Eliminar            ||\n|| 4: Mostrar todo        ||\n|| 5: Cerrar Programa     ||\n||------------------------||\n")
    if select == "1":
        add(input("Escribe el nombre: "),
            input("Escribe la especie: "),
            input("Escribe el tipo de alimento: "),
            int(input("Escribe el tiempo necesario que debe estar afuera (Minutos): ")),
            int(input("Escribe el tiempo entre cada comida (Minutos): ")),
            int(input("Cantidad de vacunas diarias: ")))
    elif select == "2":
        read(input("Buscar: "))
    elif select == "3":
        delete(input("Eliminar: "))
    elif select == "4":
        show()
    elif select == "5":
        print("Buenas Noches!")
        break
    else:
        print("Dato mal ingresado")
        break