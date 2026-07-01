NOTA_MINIMA_APROBACION = 4.0


def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Actualizar estados")
    print("5. Mostrar estudiantes")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    while True:
        opcion = input("Seleccione una opción: ").strip()
        if opcion.isdigit() and 1 <= int(opcion) <= 6:
            return int(opcion)
        print("Opción inválida. Ingrese un número entero entre 1 y 6.")


def validar_nombre(nombre):
    return nombre.strip() != ""


def validar_edad(edad_texto):
    return edad_texto.strip().isdigit() and int(edad_texto) > 0


def validar_nota(nota_texto):
    try:
        nota = float(nota_texto)
        return 1.0 <= nota <= 7.0
    except ValueError:
        return False


def agregar_estudiante(lista_estudiantes):
    nombre = input("Ingrese el nombre del estudiante: ")
    if not validar_nombre(nombre):
        print("Error: el nombre no puede estar vacío ni contener solo espacios.")
        return

    edad_texto = input("Ingrese la edad del estudiante: ")
    if not validar_edad(edad_texto):
        print("Error: la edad debe ser un número entero mayor que cero.")
        return

    nota_texto = input("Ingrese la nota del estudiante: ")
    if not validar_nota(nota_texto):
        print("Error: la nota debe ser un número decimal entre 1.0 y 7.0.")
        return

    estudiante = {
        "nombre": nombre.strip(),
        "edad": int(edad_texto),
        "nota": float(nota_texto),
        "aprobado": False
    }
    lista_estudiantes.append(estudiante)
    print(f"Estudiante '{estudiante['nombre']}' agregado con éxito.")


def opcion_pendiente():
    print("Esta opción se implementará en la próxima clase.")


def actualizar_estados(lista_estudiantes):
    for estudiante in lista_estudiantes:
        estudiante["aprobado"] = estudiante["nota"] >= NOTA_MINIMA_APROBACION


def mostrar_estudiantes(lista_estudiantes):
    actualizar_estados(lista_estudiantes)

    print("\n=== LISTA DE ESTUDIANTES ===")
    if not lista_estudiantes:
        print("No hay estudiantes registrados.")
        return

    for estudiante in lista_estudiantes:
        estado = "APROBADO" if estudiante["aprobado"] else "REPROBADO"
        print()
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Edad: {estudiante['edad']}")
        print(f"Nota: {estudiante['nota']}")
        print(f"Estado: {estado}")
        print("*" * 45)


def programa_principal():
    lista_estudiantes = []

    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            agregar_estudiante(lista_estudiantes)
        elif opcion == 2:
            opcion_pendiente()
        elif opcion == 3:
            opcion_pendiente()
        elif opcion == 4:
            actualizar_estados(lista_estudiantes)
            print("Estados actualizados con éxito.")
        elif opcion == 5:
            mostrar_estudiantes(lista_estudiantes)
        elif opcion == 6:
            print("Gracias por usar el sistema. Vuelva Pronto")
            break


programa_principal()
