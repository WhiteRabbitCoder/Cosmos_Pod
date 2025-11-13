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
    print("Función 'modificar_pacientes' no implementada.")
    # Ejemplo de uso de la función de búsqueda por ID:
    # pid = input("Ingrese el ID del paciente a modificar: ")
    # paciente = obtener_paciente_por_id(pid)
    # if paciente:
    #     print(f"Modificando a: {paciente.get('nombre')}")
    #     # ...lógica de modificación...
    # else:
    #


def eliminar_pacientes():
    print("Función 'eliminar_pacientes' no implementada.")


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
