from Pacientes_Constante import Pacientes_constantes
pacientes = Pacientes_constantes()

def eliminar_pacientes():
    print("\nBienvenido al apartado de eliminar pacientes")

id_paciente=input("Ingrese el ID del paciente a eliminar ")

if id_paciente in pacientes:
    print(f"\nPaciente encontrado: ")
    print(f"Nombre: {pacientes[id_paciente]}['nombre']")
    print(f"Edad: {pacientes[id_paciente]['edad']}")

confirmacion = input("\n ")