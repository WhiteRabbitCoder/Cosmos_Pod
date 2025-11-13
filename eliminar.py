from Pacientes_Constante import Pacientes_constantes
pacientes = Pacientes_constantes()

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

eliminar_pacientes()

for id_paciente, datos in pacientes.items():
    print(f"ID: {id_paciente}  |   Nombre:   {datos['nombre']}  |  Diagnostico:  {datos['diagnostico']}")
