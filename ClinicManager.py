from Pacientes_Constante import Pacientes_constantes

# Carga los datos iniciales de los pacientes
pacientes = Pacientes_constantes()


def buscar_pacientes():
    """
    Pide una consulta y busca coincidencias parciales en ID, nombre y diagnóstico.
    Muestra una lista de todos los que coinciden.
    """
    consulta = input("\nIngrese el ID, nombre o diagnóstico a buscar: ").strip().upper()

    if not consulta:
        print("La consulta está vacía.")
        return

    resultados = []
    # Itera sobre el diccionario principal. 'pid' es la clave (ID), 'data' es el diccionario anidado.
    for pid, data in pacientes.items():
        nombre_lower = data.get("nombre", "")
        diag_lower = data.get("diagnostico", "")
        id_lower = str(pid)

        if consulta in nombre_lower or consulta in diag_lower or consulta in id_lower:
            resultados.append((pid, data))

    if not resultados:
        print("No se encontraron pacientes que coincidan con la búsqueda.")
    else:
        print(f"\nSe encontraron {len(resultados)} coincidencias:")
        for pid, data in resultados:
            print(f"- ID: {pid}, Nombre: {data.get('nombre')}, Diagnóstico: {data.get('diagnostico')}")


def obtener_paciente_por_id(id_paciente: str):
    return pacientes.get(id_paciente)


def ingresar_pacientes():
    print("Función 'ingresar_pacientes' no implementada.")


def mostrar_pacientes():
    """
    Muestra una lista de todos los pacientes registrados.
    """
    print("\n--- Listado de Pacientes Registrados ---")
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    for pid, data in pacientes.items():
        print(f"ID: {pid}, Nombre: {data.get('nombre')}, Diagnóstico: {data.get('diagnostico')}")


def modificar_pacientes():

    def modificar_edad():
        id_paciente = input("Ingrese el ID del paciente: ")
        if id_paciente not in pacientes:
            print("ID no encontrado.\n")
            return

        print("Edad actual:", pacientes[id_paciente]["edad"])
        nueva_edad = input("Ingrese la nueva edad: ")

        confirmar = input(f"¿Confirma cambiar la edad a {nueva_edad}? (s/n): ").lower()
        if confirmar == "s":
            pacientes[id_paciente]["edad"] = nueva_edad
            print("Edad actualizada.")
        else:
            print("Cambio cancelado.")

        print("Edad final:", pacientes[id_paciente]["edad"], "\n")

    def modificar_diag():
        id_paciente = input("Ingrese el ID del paciente: ")
        if id_paciente not in pacientes:
            print("ID no encontrado.\n")
            return

        print("Diagnóstico actual:", pacientes[id_paciente]["diagnostico"])
        nuevo_diag = input("Ingrese el nuevo diagnóstico: ")

        confirmar = input(f"¿Confirma cambiar el diagnóstico a '{nuevo_diag}'? (s/n): ").lower()
        if confirmar == "s":
            pacientes[id_paciente]["diagnostico"] = nuevo_diag
            print("Diagnóstico actualizado.")
        else:
            print("Cambio cancelado.")

        print("Diagnóstico final:", pacientes[id_paciente]["diagnostico"], "\n")

    def agregar_evento():
        id_paciente = input("Ingrese el ID del paciente: ")
        if id_paciente not in pacientes:
            print("ID no encontrado.\n")
            return

        print("Historial actual:")
        for evento in pacientes[id_paciente]["historial"]:
            print("-", evento)

        nuevo_evento = input("Nuevo evento: ")

        confirmar = input("¿Agregar este evento? (s/n): ").lower()
        if confirmar == "s":
            pacientes[id_paciente]["historial"].append(nuevo_evento)
            print("Evento agregado.")
        else:
            print("Cambio cancelado.")

        print("Historial final:", pacientes[id_paciente]["historial"], "\n")

    def menu():
        while True:
            print("\n MENÚ DE MODIFICACIÓN ")
            print("1. Modificar edad")
            print("2. Modificar diagnóstico")
            print("3. Agregar evento al historial")
            print("4. Ver datos del paciente")
            print("5. Salir")

            opcion = input("Opción: ")

            if opcion == "1":
                modificar_edad()
            elif opcion == "2":
                modificar_diag()
            elif opcion == "3":
                agregar_evento()
            elif opcion == "4":
                ID = input("ID del paciente: ")
                if ID in pacientes:
                    print("Datos:", pacientes[ID], "\n")
                else:
                    print("ID no encontrado.\n")
            elif opcion == "5":
                break
            else:
                print("Opción inválida.\n")

    menu()

def eliminar_pacientes():
    print("\nBienvenido al apartado de eliminar pacientes")

    id_paciente=input("Ingrese el ID del paciente a eliminar ")

    if id_paciente in pacientes:
        print(f"\nPaciente encontrado: ")
        print(f"Nombre: {pacientes[id_paciente]}['nombre']")
        print(f"Edad: {pacientes[id_paciente]['edad']}")
    
        confirmacion = input("\n¿Estas seguro de eliminar el paciente?(s/n): ").lower()

        if confirmacion == "s":
            del pacientes[id_paciente]
            print("Paciente eliminado correctamente")

        else:
            print("Eliminacion cancelada")

    else:
        print("Error: No se encontro paciente con ese ID")   

for id_paciente, datos in pacientes.items():
    print(f"ID: {id_paciente}  |   Nombre:   {datos['nombre']}  |  Diagnostico:  {datos['diagnostico']}")
   


def exportar_pacientes():
    print("Función 'exportar_pacientes' no implementada.")


def importar_pacientes():
    print("Función 'importar_pacientes' no implementada.")


def main_menu():
    print("\n\n¡Bienvenido a Clinic Manager de Riwi - By Cosmos!")
    while True:
        print("\n¿Qué desea hacer el día de hoy?")
        print("1. Ingresar pacientes")
        print("2. Buscar pacientes")
        print("3. Mostrar todos los pacientes registrados")
        print("4. Modificar pacientes")
        print("5. Eliminar pacientes")
        print("6. Exportar datos de pacientes")
        print("7. Importar datos de pacientes")
        print("0. Salir")
        menu = input("Por favor, ingrese la opción que desea (0-7): ").strip()

        match menu:
            case "0":
                print("Saliendo.")
                break
            case "1":
                ingresar_pacientes()
            case "2":
                buscar_pacientes()
            case "3":
                mostrar_pacientes()
            case "4":
                modificar_pacientes()
            case "5":
                eliminar_pacientes()
            case "6":
                exportar_pacientes()
            case "7":
                importar_pacientes()
            case _:
                print("Opción inválida, intente nuevamente.")


if __name__ == "__main__":
    main_menu()
