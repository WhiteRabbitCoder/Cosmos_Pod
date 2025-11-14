from collections import Counter

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
        nombre = data.get("nombre", "")
        diagnostico = data.get("diagnostico", "")
        if consulta in nombre or consulta in diagnostico or consulta in pid:
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


def mostrar_pacientes(list):
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


def reportes_generales():
    opc = -1
    while opc != 0:
        try:
            print("\n\nLos reportes disponibles son: ")
            print("1. Pacientes mayores de 60 años. ")
            print("2. Diagnosticos más frecuentes. ")
            print("3. Cantidad total de pacientes registrados. ")
            print("0. Volver al menú principal ")
            opc = input("Ingrese la opción a la que desea ingresar: ")
            match opc:
                case "0":
                    opc = 0
                case "1":
                    resultado = []
                    for pid, data in pacientes.items():
                        if data.get("edad") >= 60:
                            resultado.append((pid, data))
                    for pid, data in resultado:
                        print(f"\nEl paciente {data.get('nombre')} tiene {data.get('diagnostico')}.")
                case "2":
                    diagnosticos = [data.get("diagnostico") for _,data in pacientes.items() if data.get("diagnostico")]
                    if not diagnosticos:
                        print("No hay diagnosticos registrados")
                    else:
                        conteo_diagnostico = Counter(diagnosticos).most_common(5)
                        print("\n\nLos 5 diagnosticos más comunes son: ")
                        for diagnostico, frecuencia in conteo_diagnostico:
                            print(f"- {diagnostico}, con {frecuencia} diagnostico. ")
                case "3":
                    print(len(pacientes.keys()))
                case _:
                    print("\nLo lamento, ingrese una opción correcta. ")

        except KeyboardInterrupt:
            print("\n\nVolviendo al menú principal... ")

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
        print("8. Reportes generales")
        print("0. Salir")
        menu = input("Por favor, ingrese la opción que desea (0-8): ").strip()

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
            case "8":
                reportes_generales()
            case _:
                print("Opción inválida, intente nuevamente.")


if __name__ == "__main__":
    main_menu()
