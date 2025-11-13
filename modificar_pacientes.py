from Pacientes_Constante import Pacientes_constantes
pacientes = Pacientes_constantes()

def modificar_edad(edad,ID):
    for id_paciente in pacientes.keys():
        if id_paciente == ID:
            print(pacientes[id_paciente]["edad"])
            input(f"Desea modificar su edad actual que es {edad} (s/n) ")
            pacientes[id_paciente]["edad"]=edad
            print(pacientes[id_paciente]["edad"])
            

modificar_edad(input("Ingrese la edad modificada "), input("Ingrese el id ").upper)

def modificar_diag(diagnostico,ID):
    for id_paciente in pacientes.keys():
        if id_paciente == ID:
            print(pacientes[id_paciente]["diagnostico"])
            pacientes[id_paciente]["diagnostico"]=diagnostico
            print(pacientes[id_paciente]["diagnostico"])

modificar_diag(input("Ingrese el diagnostico a modificar  "), input("Ingrese el id ").upper)
